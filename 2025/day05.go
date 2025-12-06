package main

import (
	"fmt"
	"slices"
	"strings"
)

// Solve times:
// Part 1: 6:06
// Part 2: 8:07
// Total time: 14:13

type Range struct {
	start int
	end   int
}

func day05() {
	input := strings.Split(ReadInput("day05"), "\n")

	ranges := []Range{}
	ingredients := []int{}

	doneRanges := false
	for _, line := range input {
		if line == "" {
			doneRanges = true
			continue
		}
		if doneRanges {
			var ingredient int
			fmt.Sscanf(line, "%d", &ingredient)
			ingredients = append(ingredients, ingredient)
		} else {
			var start, end int
			fmt.Sscanf(line, "%d-%d", &start, &end)
			ranges = append(ranges, Range{start, end})
		}
	}

	part1 := 0
	for _, ingredient := range ingredients {
		valid := false
		for _, r := range ranges {
			if ingredient >= r.start && ingredient <= r.end {
				valid = true
				break
			}
		}
		if valid {
			part1 += 1
		}
	}

	fmt.Printf("Part 1: %d\n", part1)

	slices.SortFunc(ranges, func(a, b Range) int {
		return a.start - b.start
	})

	part2 := 0
	max := 0
	for _, r := range ranges {
		if r.end < max {
			continue
		}
		if r.start <= max {
			r.start = max + 1
		}
		part2 += r.end - r.start + 1
		max = r.end
	}

	fmt.Printf("Part 2: %d\n", part2)
}
