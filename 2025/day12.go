package main

import (
	"fmt"
	"strconv"
	"strings"
)

func day12() {
	input := strings.Split(ReadInput("day12"), "\n")
	input = input[30:]

	var part1 int
	for _, line := range input {
		dim, gifts, _ := strings.Cut(line, ": ")
		var l, w int
		fmt.Sscanf(dim, "%dx%d", &l, &w)
		var giftCount int
		for _, g := range strings.Split(gifts, " ") {
			x, _ := strconv.Atoi(g)
			giftCount += x
		}
		if l*w/9 >= giftCount {
			part1++
		}
	}

	fmt.Println("Part 1:", part1)
	fmt.Println("Part 2: Merry Christmas!")
}
