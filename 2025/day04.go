package main

import (
	"fmt"
	"strings"
)

func day04() {
	input := strings.Split(ReadInput("day04"), "\n")
	rolls := map[int]struct{}{}
	for i, line := range input {
		for j, char := range line {
			if char == '@' {
				rolls[i*1000+j] = struct{}{}
			}
		}
	}

	part1 := 0
	part2 := 0
	for {
		remove := []int{}
		for k := range rolls {
			i := k / 1000
			j := k % 1000
			count := 0
			for di := -1; di <= 1; di++ {
				for dj := -1; dj <= 1; dj++ {
					if di == 0 && dj == 0 {
						continue
					}
					ni := i + di
					nj := j + dj
					if _, ok := rolls[ni*1000+nj]; ok {
						count++
					}
				}
			}
			if count < 4 {
				remove = append(remove, k)
			}
		}
		if len(remove) == 0 {
			break
		}
		if part1 == 0 {
			part1 = len(remove)
		}
		part2 += len(remove)
		for _, k := range remove {
			delete(rolls, k)
		}
	}

	fmt.Printf("Part 1: %d\n", part1)
	fmt.Printf("Part 2: %d\n", part2)
}
