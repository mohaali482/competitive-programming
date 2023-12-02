package main

import (
	"bufio"
	"fmt"
	"os"

	cubeconundrum "github.com/mohaali482/competitive-programming/advent_of_code_2023/cube_conundrum"
)

func main() {
	// trebuchet_solution()
	// cube_conundrum()
	cube_conundrum2()
}

// func trebuchet_solution() {
// 	file, err := os.Open("trebuchet/input.txt")
// 	if err != nil {
// 		panic(err)
// 	}
// 	defer file.Close()
// 	scanner := bufio.NewScanner(file)
// 	ans := 0
// 	var num int
// 	for scanner.Scan() {
// 		num, _ = strconv.Atoi(trebuchet.Solution2(scanner.Text()))
// 		ans += num
// 	}

// 	fmt.Println(ans)
// }

// func cube_conundrum() {
// 	file, err := os.Open("cube_conundrum/input.txt")
// 	if err != nil {
// 		panic(err)
// 	}
// 	defer file.Close()
// 	scanner := bufio.NewScanner(file)
// 	ans := 0
// 	var num int
// 	for scanner.Scan() {
// 		num = cubeconundrum.Solution(scanner.Text())
// 		ans += num
// 	}

// 	fmt.Println(ans)
// }

func cube_conundrum2() {
	file, err := os.Open("cube_conundrum/input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	ans := 0
	var num int
	for scanner.Scan() {
		num = cubeconundrum.Solution2(scanner.Text())
		ans += num
	}

	fmt.Println(ans)
}
