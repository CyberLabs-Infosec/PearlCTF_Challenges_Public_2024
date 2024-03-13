package hook

import (
	"fmt"
	"net/http"
	"os"
)

func checkHandle(w http.ResponseWriter, r *http.Request) {
	token := r.URL.Query()["token"][0]
	fmt.Println(token)
	os.Exit(0)
}

func Run() {
	checkHandler := http.HandlerFunc(checkHandle)
	http.Handle("/check", checkHandler)
	http.ListenAndServe(":6969", nil)
}