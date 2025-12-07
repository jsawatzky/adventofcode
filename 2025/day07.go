package main

import (
	"fmt"
	"strings"
)

// Solve times:
// Part 1: 11:15
// Part 2: 8:06
// Total time: 19:21

type TachyonState struct {
	Row int
	Col int
}

func day07() {
	input := strings.Split(ReadInput("day07"), "\n")

	startCol := strings.IndexRune(input[0], 'S')

	beams := map[int]struct{}{}
	beams[startCol] = struct{}{}

	part1 := 0
	for row := 1; row < len(input); row++ {
		newBeams := map[int]struct{}{}
		for col := range beams {
			if input[row][col] == '^' {
				part1++
				if col > 0 {
					newBeams[col-1] = struct{}{}
				}
				if col < len(input[row])-1 {
					newBeams[col+1] = struct{}{}
				}
			} else {
				newBeams[col] = struct{}{}
			}
		}
		beams = newBeams
	}

	fmt.Println("Part 1:", part1)

	memo := map[TachyonState]int{}
	var processTachyon func(col int, row int) int
	processTachyon = func(col int, row int) int {
		if row == len(input) {
			return 1
		}
		state := TachyonState{Row: row, Col: col}
		if val, ok := memo[state]; ok {
			return val
		}
		if input[row][col] == '^' {
			total := 0
			if col > 0 {
				total += processTachyon(col-1, row+1)
			}
			if col < len(input[row])-1 {
				total += processTachyon(col+1, row+1)
			}
			memo[state] = total
			return total
		} else {
			total := processTachyon(col, row+1)
			memo[state] = total
			return total
		}
	}

	part2 := processTachyon(startCol, 1)
	fmt.Println("Part 2:", part2)
}
