package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	fmt.Println(solution2())
}

func solve(nodes []string, instruction string, step int, graph map[string][]string, i int) int {
	if i == 1_000_000 {
		fmt.Println(nodes, step, i)
		return 0
	}
	flag := true
	for _, node := range nodes {
		if node[len(node)-1] != 'Z' {
			flag = false
			break
		}
	}
	if flag {
		return 1
	}

	node_left := make([]string, 0)
	node_right := make([]string, 0)
	for _, node := range nodes {
		node_left = append(node_left, graph[node][0])
		node_right = append(node_right, graph[node][1])
	}
	if step == len(instruction) {
		step = 0
	}

	if instruction[step] == 'L' {
		return solve(node_left, instruction, step+1, graph, i+1) + 1
	}

	return solve(node_right, instruction, step+1, graph, i+1) + 1
}

func solution2() int {
	file, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	lines := make([]string, 0)

	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	instruction := strings.TrimSpace(lines[0])
	lines = lines[2:]
	graph := make(map[string][]string)
	for _, line := range lines {
		line = strings.TrimSpace(line)
		start_end := strings.Split(line, "=")
		start := strings.TrimSpace(start_end[0])
		end := strings.TrimSpace(start_end[1])
		left := strings.Split(end, ",")[0]
		right := strings.Split(end, ",")[1]
		left = strings.TrimSpace(left[1:])
		right = strings.TrimSpace(right[:len(right)-1])
		graph[start] = []string{left, right}
	}
	start_nodes := make([]string, 0)
	for k := range graph {
		if k[len(k)-1] == 'A' {
			start_nodes = append(start_nodes, k)
		}
	}

	// return solve(start_nodes, instruction, 0, graph, i) - 1

	var index int
	var i int
	for {
		if i%1_000_000_0 == 0 {
			fmt.Println(start_nodes, i, index)
		}
		for idx, node := range start_nodes {
			if instruction[index%len(instruction)] == 'L' {
				start_nodes[idx] = graph[node][0]
			} else {
				start_nodes[idx] = graph[node][1]
			}
		}
		index++
		i++

		flag := true
		for _, node := range start_nodes {
			if node[len(node)-1] != 'Z' {
				flag = false
			}
		}

		if flag {
			break
		}
	}

	return i

}
