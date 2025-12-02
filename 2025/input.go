package main

import (
	"fmt"
	"os"
	"strings"
)

func ReadInputLines(file string) []string {
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
	lines := strings.Split(strings.TrimRight(string(data), "\n"), "\n")
	return lines
}
