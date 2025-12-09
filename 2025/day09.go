package main

import (
	"fmt"
	"math"
	"strings"
)

// Solve times:
// Part 1: 6:56
// Part 2: 1:01:20 (paused)
// Total time: ????

type Tile struct {
	X, Y int
}

func day09() {
	input := strings.Split(ReadInput("day09"), "\n")

	redTiles := []Tile{}

	for _, line := range input {
		var x, y int
		fmt.Sscanf(line, "%d,%d", &x, &y)
		redTiles = append(redTiles, Tile{x, y})
	}

	part1 := 0
	part2 := 0
	for i, tile1 := range redTiles {
		for j, tile2 := range redTiles {
			if i >= j {
				continue
			}
			area := math.Abs(float64(tile1.X-tile2.X+1)) * math.Abs(float64(tile1.Y-tile2.Y+1))
			part1 = int(math.Max(area, float64(part1)))

			// How the fuck?
		}
	}

	fmt.Println("Part 1:", part1)
	fmt.Println("Part 2:", part2)

}
