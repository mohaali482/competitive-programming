package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"

	"github.com/mohaali482/competitive-programming/advent_of_code_2023/trebuchet"
)

func main() {
	file, err := os.Open("trebuchet/input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	ans := 0
	var num int
	for scanner.Scan() {
		num, _ = strconv.Atoi(trebuchet.Solution2(scanner.Text()))
		ans += num
	}

	fmt.Println(ans)
}
