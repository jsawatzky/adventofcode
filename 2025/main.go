package main

import (
	"fmt"
	"time"

	"github.com/spf13/pflag"
)

var TestMode bool = false

func main() {
	pflag.BoolVarP(&TestMode, "test", "t", false, "Enable test mode")
	pflag.Parse()

	args := pflag.Args()

	if len(args) > 1 {
		fmt.Println("Usage: program [--test|-t] [day]")
		return
	}

	var day string
	if len(args) == 1 {
		day = args[0]
	} else {
		day = fmt.Sprintf("%02d", time.Now().Day())
	}

	switch day {
	case "01":
		day01()
	default:
		fmt.Println("Day not implemented")
	}
}
