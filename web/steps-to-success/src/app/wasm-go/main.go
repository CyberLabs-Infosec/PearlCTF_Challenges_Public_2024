package main

import (
	b64 "encoding/base64"
	"strings"
)

const SECRET = "my_key"

func main() {}

func EncryptDecrypt(input, key string) string {
	kL := len(key)

	var tmp []string
	for i := 0; i < len(input); i++ {
		tmp = append(tmp, string(input[i]^key[i%kL]))
	}
	return strings.Join(tmp, "")
}

//export getCode_1
func GetCode_1(base64_str string) *byte {
	var buffer [1024]byte

	obfuscated, _ := b64.StdEncoding.DecodeString(base64_str)

	code := EncryptDecrypt(string(obfuscated), SECRET)
	copy(buffer[:], []byte(code))

	return &buffer[0]
}

//export getBuffer
func GetBuffer() *byte {
	var buffer [1024]byte
	return &buffer[0]
}
