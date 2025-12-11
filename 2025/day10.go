package main

import (
	"fmt"
	"math"
	"math/bits"
	"strings"
	"sync"

	"github.com/draffensperger/golp"
)

// Solve times:
// Part 1: 29:29
// Part 2: ~2:30:00
// Total time: ~3:00:00

func day10() {
	input := strings.Split(ReadInput("day10"), "\n")

	convertLightDiagram := func(line string) int {
		line = strings.Trim(line, "[]")
		var ret int
		for i, ch := range line {
			if ch == '#' {
				ret |= 1 << i
			}
		}
		return ret
	}

	convertButton := func(line string) int {
		line = strings.Trim(line, "()")
		var ret int
		nums := strings.SplitSeq(line, ",")
		for num := range nums {
			var n int
			fmt.Sscanf(num, "%d", &n)
			ret |= 1 << n
		}
		return ret
	}

	convertLevels := func(line string) []int {
		line = strings.Trim(line, "{}")
		parts := strings.Split(line, ",")
		ret := make([]int, len(parts))
		for i, part := range parts {
			fmt.Sscanf(part, "%d", &ret[i])
		}
		return ret
	}

	part1 := 0
	p2Results := make(chan int)
	var wg sync.WaitGroup
	for _, line := range input {
		parts := strings.Split(line, " ")
		lightDiagram := convertLightDiagram(parts[0])
		buttons := []int{}
		for _, btnStr := range parts[1 : len(parts)-1] {
			buttons = append(buttons, convertButton(btnStr))
		}
		levels := convertLevels(parts[len(parts)-1])

		minCount := len(buttons) + 1
		for i := range 1 << len(buttons) {
			d := 0
			for j := range buttons {
				if (i>>j)&1 == 1 {
					d ^= buttons[j]
				}
			}
			if d == lightDiagram && bits.OnesCount(uint(i)) < minCount {
				minCount = bits.OnesCount(uint(i))
			}
		}
		part1 += minCount

		wg.Add(1)
		go func(wg *sync.WaitGroup, buttons []int, levels []int) {
			defer wg.Done()

			lp := golp.NewLP(len(levels), len(buttons))
			v := make([]float64, len(buttons))
			for i := range v {
				v[i] = 1
				lp.SetInt(i, true)
			}
			lp.SetObjFn(v)
			for i, lvl := range levels {
				vals := make([]float64, len(buttons))
				for j := range buttons {
					if (buttons[j]>>i)&1 == 1 {
						vals[j] = 1
					} else {
						vals[j] = 0
					}
				}
				lp.AddConstraint(vals, golp.EQ, float64(lvl))
			}
			typ := lp.Solve()
			if typ != golp.OPTIMAL {
				panic("No optimal solution found")
			}

			p2Results <- int(math.Round(lp.Objective()))
		}(&wg, buttons, levels)
	}

	fmt.Println("Part 1:", part1)

	go func(wg *sync.WaitGroup) {
		wg.Wait()
		close(p2Results)
	}(&wg)

	var part2 int
	for res := range p2Results {
		part2 += res
	}
	fmt.Println("Part 2:", part2)
}
