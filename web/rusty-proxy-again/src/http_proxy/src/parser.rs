use std::{collections::HashMap, error::Error, fmt};

const FORWARD_IP:   &str = "0.0.0.0";
const FORWARD_PORT: &str = "5000";

#[allow(warnings)]
#[derive(Debug)]
pub enum REQ_METHOD {
    GET,
    POST,
}

#[derive(Debug)]
struct BadReqErr(String);

impl fmt::Display for BadReqErr {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "There is an error: {}", self.0)
    }
}

impl Error for BadReqErr {}

#[allow(warnings)]
#[derive(Debug)]
pub struct HTTP_REQ {
    pub http_version: Option<String>,
    pub method: REQ_METHOD,
    pub path: Option<String>,
    pub headers: HashMap<String, String>,
}

impl HTTP_REQ {
    pub fn new() -> HTTP_REQ {
        let http_req = HTTP_REQ {
            http_version: None,
            method: REQ_METHOD::GET,
            path: None,
            headers: HashMap::new(),
        };

        http_req
    }

    fn reward() -> String {
        let mut i = 0;
        let obfucated = "pdcqh~Q4deUj~>Qv dMRKgsaGnsA#`".as_bytes().into_iter();
        let mut reward: Vec<u8> =  vec![];

        for chr in obfucated {
            reward.push(*chr ^ i);
            i += 1;
        }

        String::from_utf8(reward).unwrap()
    }

    fn set_head(&mut self, head: &String) {
        let head_split = head.split(' ').collect::<Vec<&str>>();

        self.http_version = Some(head_split[2].to_string());

        if self.http_version == Some("HTTP/2".to_string()) {
            self.http_version = Some("HTTP/2.0".to_string());
        }

        match head_split[0] {
            "GET" => self.method = REQ_METHOD::GET,
            "POST" => self.method = REQ_METHOD::POST,
            _ => (),
        }

        self.path = Some(head_split[1].to_string());
    }

    fn body_length(&mut self, body: String) -> String {
        body.len().to_string()
    }

    pub fn parse(&mut self, raw_req: &String) -> Result<(), Box<dyn Error>> {
        HTTP_REQ::reward();
        let req = raw_req.split("\r\n").collect::<Vec<&str>>();
        self.set_head(&req[0].to_string());

        let mut ind = 1;

        while req[ind].to_string() != "" {
            let header_split = req[ind].split(":").collect::<Vec<&str>>();

            let header_key = header_split[0].trim().to_lowercase();
            let header_val = header_split[1].trim().to_string();

            if !self.headers.contains_key(&header_key) {
                self.headers.insert(header_key, header_val);
            } else {
                *self.headers.get_mut(&header_key).unwrap() = header_val;
            }

            ind += 1;
        }

        match self.method {
            REQ_METHOD::POST => {
                let body_len = self.body_length(req[ind + 1].to_string());
                let cl = "content-length".to_string();
                if !self.headers.contains_key(&cl) {
                    self.headers.insert(cl, body_len);
                } else {
                    *self.headers.get_mut(&cl).unwrap() = body_len;
                }

                if !self.headers.contains_key("content-type") {
                    return Err(Box::new(BadReqErr("Content type expected in the header".into())))
                }
            },
            _ => (),
        }

        Ok(())
    }

    pub fn create_raw(&self) -> String {
        let mut req = "".to_string();

        match self.method {
            REQ_METHOD::GET => {
                req.push_str(&format!("GET {} {}\r\n", &self.path.as_ref().unwrap(), &self.http_version.as_ref().unwrap()));
                req.push_str(&format!("Host: {}:{}\r\n", FORWARD_IP, FORWARD_PORT));

                req.push_str("\r\n");
            },
            REQ_METHOD::POST => {
                req.push_str(&format!("POST {} {}\r\n", &self.path.as_ref().unwrap(), &self.http_version.as_ref().unwrap()));
                req.push_str(&format!("Host: {}:{}\r\n", FORWARD_IP, FORWARD_PORT));
                req.push_str(&format!("Content-Length: {}\r\n", &self.headers["content-length"]));
                req.push_str(&format!("Content-Type: {}\r\n", &self.headers["content-type"]));

                req.push_str("\r\n");
            }
        }

        req
    }
}