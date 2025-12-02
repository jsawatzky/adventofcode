package main

import (
	"fmt"
)

func day01() {
	input := ReadInputLines("day01")

	angle := 50
	part1 := 0
	part2 := 0
	for _, line := range input {
		dir := line[0]
		amt := 0
		_, err := fmt.Sscanf(line[1:], "%d", &amt)
		if err != nil {
			panic(err)
		}

		part2 += amt / 100
		amt %= 100

		switch dir {
		case 'L':
			angle -= amt
		case 'R':
			angle += amt
		default:
			panic("invalid direction")
		}

		if (angle <= 0 && angle != -amt) || angle > 99 {
			part2++
		}

		angle = (angle%100 + 100) % 100 // keep angle in [0, 99]

		if angle == 0 {
			part1++
		}
	}

	fmt.Printf("Part 1: %d\n", part1)
	fmt.Printf("Part 2: %d\n", part2)
}
