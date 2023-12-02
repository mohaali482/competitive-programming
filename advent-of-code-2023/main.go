package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	trebuchet()
}

func trebuchet() {
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
