package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func find(r [][2]int64, dictionary map[int64][2]int64) [][2]int64 {
	ans := make([][2]int64, 0)
	for k, v := range dictionary {
		dest, src, sz := k, v[0], v[1]
		src_end := src + sz
		nr := make([][2]int64, 0)
		for len(r) > 0 {
			st, ed := r[0][0], r[0][1]
			r = r[1:]

			before := [2]int64{st, min(ed, src)}
			inter := [2]int64{max(st, src), min(src_end, ed)}
			after := [2]int64{max(src_end, st), ed}

			if before[1] > before[0] {
				nr = append(nr, before)
			}
			if inter[1] > inter[0] {
				ans = append(ans, [2]int64{inter[0] - src + dest, inter[1] - src + dest})
			}
			if after[1] > after[0] {
				nr = append(nr, after)
			}
		}
		r = nr
	}
	return append(ans, r...)
}

func solution() int64 {
	seeds := make([]int64, 0)
	seedToSoil := make(map[int64][2]int64)
	soilToFertilizer := make(map[int64][2]int64)
	fertilizerToWater := make(map[int64][2]int64)
	waterToLight := make(map[int64][2]int64)
	lightToTemperature := make(map[int64][2]int64)
	temperatureToHumidity := make(map[int64][2]int64)
	humidityToLocation := make(map[int64][2]int64)
	windows := map[int64]map[int64][2]int64{
		1: seedToSoil, 2: soilToFertilizer, 3: fertilizerToWater, 4: waterToLight, 5: lightToTemperature, 6: temperatureToHumidity, 7: humidityToLocation,
	}

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

	counter := int64(1)
	temp := strings.Fields(lines[0])
	for _, val := range temp[1:] {
		num, _ := strconv.Atoi(val)
		seeds = append(seeds, int64(num))
	}

	win := windows[counter]
	i := 3
	for i < len(lines) {
		line := lines[i]
		if line == "" {
			counter++
			win = windows[counter]
			i += 2
		} else {
			temp := strings.Fields(line)
			x, _ := strconv.Atoi(temp[0])
			st, _ := strconv.Atoi(temp[1])
			en, _ := strconv.Atoi(temp[2])
			win[int64(x)] = [2]int64{int64(st), int64(st + en)}
			i++
		}
	}

	p2 := make([][2]int64, 0)

	for i := 0; i < len(seeds); i += 2 {
		seedRange := [][2]int64{{seeds[i], seeds[i] + seeds[i+1]}}
		soil := find(seedRange, seedToSoil)
		fertilizer := find(soil, soilToFertilizer)
		water := find(fertilizer, fertilizerToWater)
		light := find(water, waterToLight)
		temperature := find(light, lightToTemperature)
		humidity := find(temperature, temperatureToHumidity)
		location := find(humidity, humidityToLocation)
		small := [2]int64{math.MaxInt64, math.MaxInt64}

		for f := range location {
			if location[f][0] < small[0] {
				small = location[f]
			}
		}
		p2 = append(p2, small)
	}
	small := [2]int64{math.MaxInt64, math.MaxInt64}
	for f := range p2 {
		if p2[f][0] < small[0] {
			small = p2[f]
		}
	}
	fmt.Println(small)
	return 0
}

func main() {
	fmt.Println(solution())
}
