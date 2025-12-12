package main

import (
	"fmt"
	"math"
	"strings"
)

// Solve times:
// Part 1: 6:56
// Part 2: over 3 hours
// Total time: over 3 hours

type Tile struct {
	X, Y int
}

func day09() {
	input := strings.Split(ReadInput("day09"), "\n")

	redTiles := []Tile{}

	hEdges := map[int][][2]int{}
	vEdges := map[int][][2]int{}

	for i, line := range input {
		var x, y int
		fmt.Sscanf(line, "%d,%d", &x, &y)
		redTiles = append(redTiles, Tile{x, y})
		if i > 0 {
			if x == redTiles[i-1].X {
				vEdges[x] = append(vEdges[x], [2]int{int(math.Min(float64(redTiles[i-1].Y), float64(y))), int(math.Max(float64(redTiles[i-1].Y), float64(y)))})
			} else {
				hEdges[y] = append(hEdges[y], [2]int{int(math.Min(float64(redTiles[i-1].X), float64(x))), int(math.Max(float64(redTiles[i-1].X), float64(x)))})
			}
		}
	}
	if redTiles[0].X == redTiles[len(redTiles)-1].X {
		vEdges[redTiles[0].X] = append(vEdges[redTiles[0].X], [2]int{int(math.Min(float64(redTiles[0].Y), float64(redTiles[len(redTiles)-1].Y))), int(math.Max(float64(redTiles[0].Y), float64(redTiles[len(redTiles)-1].Y)))})
	} else {
		hEdges[redTiles[0].Y] = append(hEdges[redTiles[0].Y], [2]int{int(math.Min(float64(redTiles[0].X), float64(redTiles[len(redTiles)-1].X))), int(math.Max(float64(redTiles[0].X), float64(redTiles[len(redTiles)-1].X)))})
	}

	checkEdge := func(edges map[int][][2]int, fixedCoord, start, end int) bool {
		if start == end {
			return true
		}

		inside := false
		state := 0
		for k := range end {
			for _, edge := range edges[k] {
				if edge[0] < fixedCoord && edge[1] > fixedCoord { // Crossed in middle of edge
					if !inside { // was out, now in
						inside = true
					} else { // was in, now out
						if k < start {
							inside = false
						} else {
							return false // not at end, can't leave
						}
					}
				} else if fixedCoord == edge[0] { // hit corner to positive
					if inside {
						if state > 0 {
							return false
						} else if state < 0 {
							state = 0
						} else {
							state = -1
						}
					} else {
						inside = true
						state = 1
					}
				} else if fixedCoord == edge[1] { // hit corner to negative
					if inside {
						if state < 0 {
							return false
						} else if state > 0 {
							state = 0
						} else {
							state = 1
						}
					} else {
						inside = true
						state = -1
					}
				}
			}
			if k == start && !inside {
				return false
			}
		}
		return inside
	}

	part1 := 0
	part2 := 0
	for i, tile1 := range redTiles {
		for j, tile2 := range redTiles {
			if i >= j {
				continue
			}
			area := (math.Abs(float64(tile1.X-tile2.X)) + 1) * (math.Abs(float64(tile1.Y-tile2.Y)) + 1)
			part1 = int(math.Max(area, float64(part1)))

			if area <= float64(part2) {
				continue
			}

			x1 := int(math.Min(float64(tile1.X), float64(tile2.X)))
			x2 := int(math.Max(float64(tile1.X), float64(tile2.X)))
			y1 := int(math.Min(float64(tile1.Y), float64(tile2.Y)))
			y2 := int(math.Max(float64(tile1.Y), float64(tile2.Y)))

			if checkEdge(hEdges, x1, y1, y2) && checkEdge(hEdges, x2, y1, y2) && checkEdge(vEdges, y1, x1, x2) && checkEdge(vEdges, y2, x1, x2) {
				part2 = int(math.Max(area, float64(part2)))
			}
		}
	}

	fmt.Println("Part 1:", part1)
	fmt.Println("Part 2:", part2)

}
