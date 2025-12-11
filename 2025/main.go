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
	case "02":
		day02()
	case "03":
		day03()
	case "04":
		day04()
	case "05":
		day05()
	case "06":
		day06()
	case "07":
		day07()
	case "08":
		day08()
	case "09":
		day09()
	case "10":
		day10()
	case "11":
		day11()
	case "12":
		day12()
	default:
		fmt.Println("Day not implemented")
	}
}
