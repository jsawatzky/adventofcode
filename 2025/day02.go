package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/glenn-brown/golang-pkg-pcre/src/pkg/pcre"
)

func day02() {
	input := strings.Split(ReadInput("day02"), ",")

	p1Regex := pcre.MustCompile(`^(\d+?)\1$`, 0)
	p2Regex := pcre.MustCompile(`^(\d+?)\1+$`, 0)

	part1 := 0
	part2 := 0
	for _, r := range input {
		var n1, n2 int
		_, err := fmt.Sscanf(r, "%d-%d", &n1, &n2)
		if err != nil {
			panic(err)
		}

		for i := n1; i <= n2; i++ {
			s := strconv.Itoa(i)
			if p1Regex.MatcherString(s, 0).Matches() {
				part1 += i
			}
			if p2Regex.MatcherString(s, 0).Matches() {
				part2 += i
			}
		}
	}

	fmt.Printf("Part 1: %d\n", part1)
	fmt.Printf("Part 2: %d\n", part2)
}
