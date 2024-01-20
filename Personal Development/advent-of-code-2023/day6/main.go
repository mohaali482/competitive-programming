package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	timer "time"
)

func main() {
	st := timer.Now()
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

	time := make([]string, 0, len(lines[0]))
	for _, c := range strings.Split(lines[0], " ") {
		if _, err := strconv.Atoi(c); err == nil {
			time = append(time, c)
		}
	}
	distance := make([]string, 0, len(lines[0]))
	for _, c := range strings.Split(lines[1], " ") {
		if _, err := strconv.Atoi(c); err == nil {
			distance = append(distance, c)
		}
	}

	time_, _ := strconv.Atoi(strings.Join(time, ""))
	distance_, _ := strconv.Atoi(strings.Join(distance, ""))
	tot := 0
	for j := 0; j < time_+1; j++ {
		if distance_ < (time_-j)*j {
			tot += 1
		}
	}
	fmt.Println(tot)
	fmt.Println(timer.Since(st))
}
