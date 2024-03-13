package main
import (
	"fmt"
	"net"
	"os"
	"strings"
	"net/url"
)
const (
	SERVER_HOST = "localhost"
	SERVER_PORT = "5001"
	SERVER_TYPE = "tcp"
)
func main() {
	fmt.Println("Server Running...")
	server, err := net.Listen(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)
	if err != nil {
		fmt.Println("Error listening:", err.Error())
		os.Exit(1)
	}
	defer server.Close()

	fmt.Println("Listening on " + SERVER_HOST + ":" + SERVER_PORT)

	for {
		connection, err := server.Accept()
		if err != nil {
			fmt.Println("Error accepting: ", err.Error())
		}

		go processClient(connection)
	}
}
func processClient(connection net.Conn) {
	buffer := make([]byte, 1024)
	mLen, err := connection.Read(buffer)
	if err != nil {
		fmt.Println("Error reading:", err.Error())
	}
	raw_http_req := strings.Split(string(buffer[:mLen]), "\r\n")[0]
	splitted_req := strings.Split(raw_http_req, " ")

	if splitted_req[0] != "GET" {
		_, err = connection.Write([]byte("HTTP/1.1 405 Method Not Allowed\r\n\r\nCan only GET"))
		connection.Close()
		return
	}

	parsed, err := url.Parse(splitted_req[1])
	if err != nil {
		fmt.Println("Error parsing: ", err.Error())
	}

	path := parsed.Path

	if path != "/resp" {
		_, err = connection.Write([]byte("HTTP/1.1 404 Not Found\r\n\r\nNot Found"))
		connection.Close()
		return
	}
	
	args, err := url.ParseQuery(parsed.RawQuery)

	if err != nil {
		_, err = connection.Write([]byte("HTTP/1.1 500 Internal Server Error\r\n\r\nError"))
		connection.Close()
		return
	}

	body, ok := args["body"]

	if !ok {
		_, err = connection.Write([]byte("HTTP/1.1 200 OK\r\n\r\nGive me some body"))
		connection.Close()
		return
	}

	_, err = connection.Write([]byte(body[0]))
	connection.Close()
}