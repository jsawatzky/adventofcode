package main

import (
	"container/heap"
	"fmt"
	"slices"
	"strings"
)

// Solve times:
// Part 1: 16:40
// Part 2: 5:50
// Total time: 22:30

type JunctionBox struct {
	X, Y, Z int
	Circuit *Circuit
}

type Circuit struct {
	Boxes []*JunctionBox
}

type BoxDistHeap []struct {
	Dist int
	Box1 *JunctionBox
	Box2 *JunctionBox
}

func (h BoxDistHeap) Len() int           { return len(h) }
func (h BoxDistHeap) Less(i, j int) bool { return h[i].Dist < h[j].Dist }
func (h BoxDistHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *BoxDistHeap) Push(x interface{}) {
	*h = append(*h, x.(struct {
		Dist int
		Box1 *JunctionBox
		Box2 *JunctionBox
	}))
}

func (h *BoxDistHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func day08() {
	input := strings.Split(ReadInput("day08"), "\n")

	unconnectedBoxes := map[*JunctionBox]struct{}{}
	dists := &BoxDistHeap{}
	heap.Init(dists)

	for _, line := range input {
		var x, y, z int
		fmt.Sscanf(line, "%d,%d,%d", &x, &y, &z)
		box := &JunctionBox{X: x, Y: y, Z: z}
		for otherBox := range unconnectedBoxes {
			dx := box.X - otherBox.X
			dy := box.Y - otherBox.Y
			dz := box.Z - otherBox.Z
			dist := dx*dx + dy*dy + dz*dz
			heap.Push(dists, struct {
				Dist int
				Box1 *JunctionBox
				Box2 *JunctionBox
			}{Dist: dist, Box1: box, Box2: otherBox})
		}
		unconnectedBoxes[box] = struct{}{}
	}

	circuits := map[*Circuit]struct{}{}

	var i int
	maxConnections := 1000
	if TestMode {
		maxConnections = 10
	}
	for dists.Len() > 0 {
		item := heap.Pop(dists).(struct {
			Dist int
			Box1 *JunctionBox
			Box2 *JunctionBox
		})
		box1 := item.Box1
		box2 := item.Box2
		if box1.Circuit == nil && box2.Circuit == nil {
			circuit := &Circuit{Boxes: []*JunctionBox{box1, box2}}
			box1.Circuit = circuit
			box2.Circuit = circuit
			circuits[circuit] = struct{}{}
			delete(unconnectedBoxes, box1)
			delete(unconnectedBoxes, box2)
		} else if box1.Circuit != nil && box2.Circuit == nil {
			box1.Circuit.Boxes = append(box1.Circuit.Boxes, box2)
			box2.Circuit = box1.Circuit
			delete(unconnectedBoxes, box2)
		} else if box1.Circuit == nil && box2.Circuit != nil {
			box2.Circuit.Boxes = append(box2.Circuit.Boxes, box1)
			box1.Circuit = box2.Circuit
			delete(unconnectedBoxes, box1)
		} else if box1.Circuit != box2.Circuit {
			circuit1 := box1.Circuit
			circuit2 := box2.Circuit
			for _, b := range circuit2.Boxes {
				b.Circuit = circuit1
				circuit1.Boxes = append(circuit1.Boxes, b)
			}
			delete(circuits, circuit2)
		}
		i++
		if i == maxConnections {
			circuitSizes := []int{}
			for circuit := range circuits {
				circuitSizes = append(circuitSizes, len(circuit.Boxes))
			}
			slices.Sort(circuitSizes)
			slices.Reverse(circuitSizes)

			fmt.Println("Part 1:", circuitSizes[0]*circuitSizes[1]*circuitSizes[2])
		}
		if len(unconnectedBoxes) == 0 && len(circuits) == 1 {
			fmt.Println("Part 2:", box1.X*box2.X)
			break
		}
	}
}
