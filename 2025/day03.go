package main

import (
	"fmt"
	"math"
	"slices"
	"strings"
)

func day03() {
	input := strings.Split(ReadInput("day03"), "\n")

	part1 := 0
	part2 := 0
	for _, line := range input {
		bank := []int{}
		for _, c := range line {
			bank = append(bank, int(c-'0'))
		}

		part1 += maxJoltage(bank, 2)
		part2 += maxJoltage(bank, 12)
	}

	fmt.Printf("Part 1: %d\n", part1)
	fmt.Printf("Part 2: %d\n", part2)
}

func maxJoltage(bank []int, numBats int) int {
	if numBats <= 0 {
		return 0
	}
	if len(bank) == 0 {
		panic("no batteries available")
	}
	numBats--
	x := slices.Max(bank[:len(bank)-numBats])
	i := slices.Index(bank, x)
	y := maxJoltage(bank[i+1:], numBats)
	return x*int(math.Pow10(numBats)) + y
}
