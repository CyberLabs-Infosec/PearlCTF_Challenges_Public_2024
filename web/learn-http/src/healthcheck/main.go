package main

import (
	"bytes"
	"example.com/healthcheck/hook"
	"net/http"
	"net/url"
	"os"
	"time"
)

func main() {
	go hook.Run()
	go check()
	time.Sleep(30 * time.Second)
	os.Exit(1)
}

func check() {
	body, _ := url.PathUnescape(os.Args[1])
	http.Post("http://localhost:6000/check", "application/x-www-form-urlencoded", bytes.NewBuffer([]byte("body=" + body)))
}
