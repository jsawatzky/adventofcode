package main

import (
	"fmt"
	"strings"
)

func day11() {
	input := strings.Split(ReadInput("day11"), "\n")

	graph := map[string][]string{}
	for _, line := range input {
		d, outs, _ := strings.Cut(line, ": ")
		graph[d] = strings.Split(outs, " ")
	}

	var dfs func(node string) int
	dfs = func(node string) int {
		if node == "out" {
			return 1
		}
		count := 0
		for _, neighbor := range graph[node] {
			count += dfs(neighbor)
		}
		return count
	}

	part1 := dfs("you")
	fmt.Println("Part 1:", part1)

	memo := map[struct {
		n        string
		dac, fft bool
	}]int{}
	var dfs2 func(node string, dac, fft bool) int
	dfs2 = func(node string, dac, fft bool) int {
		if node == "out" {
			if dac && fft {
				return 1
			} else {
				return 0
			}
		}
		if val, ok := memo[struct {
			n        string
			dac, fft bool
		}{node, dac, fft}]; ok {
			return val
		}
		if node == "dac" {
			dac = true
		}
		if node == "fft" {
			fft = true
		}
		count := 0
		for _, neighbor := range graph[node] {
			count += dfs2(neighbor, dac, fft)
		}
		memo[struct {
			n        string
			dac, fft bool
		}{node, dac, fft}] = count
		return count
	}

	part2 := dfs2("svr", false, false)
	fmt.Println("Part 2:", part2)
}
