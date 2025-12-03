package main

import (
	"fmt"
	"os"
	"strings"
)

func ReadInput(file string) string {
	var path string
	if TestMode {
		path = fmt.Sprintf("tests/%s.txt", file)
	} else {
		path = fmt.Sprintf("inputs/%s.txt", file)
	}
	data, err := os.ReadFile(path)
	if err != nil {
		panic(err)
	}
	return strings.TrimSpace(string(data))
}
