package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
	"sync"
)

func find(key int64, dictionary map[int64][2]int64) int64 {
	for k, v := range dictionary {
		if v[0] <= key && key < v[1] {
			return k + key - v[0]
		}
	}
	return key
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

	var minLocation int64 = math.MaxInt64
	setSeeds := make(map[int64]bool)
	for i := 0; i < len(seeds); i += 2 {
		seedRange := [2]int64{seeds[i], seeds[i] + seeds[i+1]}
		for j := seedRange[0]; j < seedRange[1]; j++ {
			if !setSeeds[j] {
				setSeeds[j] = true
			}
		}
	}

	wg := sync.WaitGroup{}

	for seed := range setSeeds {
		wg.Add(1)
		go func(seed int64) {
			soil := find(seed, seedToSoil)
			fertilizer := find(soil, soilToFertilizer)
			water := find(fertilizer, fertilizerToWater)
			light := find(water, waterToLight)
			temperature := find(light, lightToTemperature)
			humidity := find(temperature, temperatureToHumidity)
			location := find(humidity, humidityToLocation)
			if location < minLocation {
				minLocation = location
			}
			wg.Done()
		}(seed)
	}

	wg.Wait()

	return minLocation
}

func main() {
	fmt.Println(solution())
}
