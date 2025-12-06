package main

import (
	"fmt"
	"strconv"
	"strings"
)

// Solve times:
// Part 1: 8:05
// Part 2: 17:51
// Total time: 25:56

func day06() {
	input := strings.Split(ReadInput("day06"), "\n")

	nums := [][]string{}
	var ops []string

	for i, line := range input {
		fields := strings.Fields(line)
		if i == len(input)-1 {
			ops = fields
		} else {
			nums = append(nums, fields)
		}
	}

	part1 := 0
	for i, op := range ops {
		res := 0
		if op == "*" {
			res = 1
		}
		for _, row := range nums {
			n, _ := strconv.Atoi(row[i])
			if op == "+" {
				res += n
			} else if op == "*" {
				res *= n
			}
		}
		part1 += res
	}

	fmt.Printf("Part 1: %d\n", part1)

	rotatedInput := []string{}
	for i := len(input[0]) - 1; i >= 0; i-- {
		newRow := []string{}
		for j := 0; j < len(input); j++ {
			if i >= len(input[j]) {
				newRow = append(newRow, " ")
				continue
			}
			newRow = append(newRow, string(input[j][i]))
		}
		rotatedInput = append(rotatedInput, strings.Join(newRow, ""))
	}

	part2 := 0
	curNums := []int{}
	for _, line := range rotatedInput {
		if strings.TrimSpace(line) == "" {
			continue
		}
		var op rune
		if line[len(line)-1] == '+' || line[len(line)-1] == '*' {
			op = rune(line[len(line)-1])
			line = line[:len(line)-1]
		}
		n, _ := strconv.Atoi(strings.TrimSpace(line))
		curNums = append(curNums, n)
		switch op {
		case '+':
			for _, n := range curNums {
				part2 += n
			}
			curNums = []int{}
		case '*':
			prod := 1
			for _, n := range curNums {
				prod *= n
			}
			part2 += prod
			curNums = []int{}
		}
	}

	fmt.Printf("Part 2: %d\n", part2)
}
