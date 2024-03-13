use std::{
    borrow::Borrow, io::{prelude::*, BufReader, Error}, net::{TcpListener, TcpStream}, sync::mpsc::Receiver, time
};

use threadpool::ThreadPool;
use std::sync::mpsc::channel;

mod parser;
use parser::HTTP_REQ;

use crate::parser::REQ_METHOD;

const PROXY_IP:   &str  = "0.0.0.0";
const PROXY_PORT: &str  = "1337";

const FORWARD_IP:   &str = "0.0.0.0";
const FORWARD_PORT: &str = "5000";

const CHUNK_SIZE: usize = 0x8000;

const WORKERS: usize = 4;

fn main() {
    let listener: TcpListener = TcpListener::bind(format!("{}:{}", PROXY_IP, PROXY_PORT)).unwrap();
    let pool = ThreadPool::new(WORKERS);

    let (sender, receiver) = channel::<String>();

    for stream in listener.incoming() {
        let mut stream: TcpStream = stream.unwrap();
        let sender_clone = sender.clone();

        pool.execute(move || {
            println!("Spawned a worker");
            let res = handle_connection(&mut stream);
            if res.is_err() {
                let resp = sender_clone.send("There was an error handling the request!!".to_string());
                if resp.is_err() {
                    println!("Error in sending signal");
                }
            } else {
                let resp = sender_clone.send("Request Complete".to_string());
                if resp.is_err() {
                    println!("Error in sending signal");
                }
            }
            println!("Worker killed");
        });

        kill_thread(&receiver);
    }
}

fn kill_thread(recv_chan: &Receiver<String>) -> String {
    let millis = time::Duration::from_millis(5000);
    let resp = recv_chan.recv_timeout(millis);
    if resp.is_err() {
        return "Request timed out!!".to_string()
    }
    return resp.unwrap()
}

fn read_stream(stream: &mut TcpStream) -> Result<String, Error> {
    let mut buf_reader: BufReader<&mut TcpStream> = BufReader::new(stream);
    let mut req: String = "".to_string();

    loop {
        let buf: &mut [u8; CHUNK_SIZE] = &mut [0; CHUNK_SIZE];
        let res: Result<usize, Error> = buf_reader.read(buf);

        if res.is_err() {
            return Err(res.unwrap_err());
        }

        req.push_str(String::from_utf8_lossy(buf).borrow());

        if buf[buf.len() - 1] == 0 {
            break;
        }
    }

    Ok(req.trim_matches(char::from(0)).to_string())
}

fn handle_connection(stream: &mut TcpStream) -> Result<(), Error> {
    println!("Got a request!");
    let read_stream_res = read_stream(stream);
    if read_stream_res.is_err() {
        let res = stream.write_all(format!("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{}", &read_stream_res.err().unwrap().to_string()).as_bytes());
        if res.is_err() {
            println!("{}", res.err().unwrap());
            return Ok(())
        }
        return Ok(())
    }

    let trimed_req = read_stream_res.unwrap();

    let mut http_req = HTTP_REQ::new();
    let res = http_req.parse(&trimed_req);

    if res.is_err() {
        let result = stream.write_all(format!("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{}", &res.err().unwrap().to_string()).as_bytes());
        println!("{}", result.err().unwrap());
        return Ok(())
    }

    match &http_req.path {
        Some(i) => {
            if i.starts_with("/flag") {
                http_req.path = Some("/no_flag_banner".to_string());
            }
        },
        _ => (),        
    }

    if (!http_req.headers.contains_key("ctf") || http_req.headers.get("ctf").unwrap() != "PearlCTF") && matches!(http_req.method, REQ_METHOD::POST) {
        let res = stream.write_all("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nInvalid post request!!".as_bytes());
        if res.is_err() {
            println!("{}", res.err().unwrap());
            return Ok(())
        }
    } else {
        let mut raw_header = trimed_req.split("\r\n\r\n").collect::<Vec<&str>>()[0].to_string();
        raw_header.push_str("\r\n\r\n");

        let body = trimed_req.replace(&raw_header, "");
        let mut forward_req = http_req.create_raw();
        forward_req.push_str(&body);

        let resp_from_host = get_resp_from_host(forward_req);

        let res = stream.write_all(resp_from_host.as_bytes());
        if res.is_err() {
            println!("{}", res.err().unwrap());
            return Ok(())
        }
    }

    Ok(())
}

fn get_resp_from_host(req: String) -> String {
    let res = TcpStream::connect(format!("{}:{}", FORWARD_IP, FORWARD_PORT));
    if res.is_err() {
        println!("{}", res.err().unwrap());
        return "".to_string()
    }
    let mut stream = res.unwrap();
    let sent = stream.write_all(req.as_bytes());

    if sent.is_err() {
        println!("{}", sent.err().unwrap());
        return "".to_string()
    }

    let read_stream_res = read_stream(&mut stream);
    if read_stream_res.is_err() {
        println!("{}", read_stream_res.err().unwrap());
        return "".to_string()
    }

    read_stream_res.unwrap()
}
