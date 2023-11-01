func minimumRefill(plants []int, capacityA int, capacityB int) int {
	var i, j, capI, capJ, counter int
	i = 0
	j = len(plants) - 1
	capI = capacityA
	capJ = capacityB
	for i <= j {
		if i == j {
			if plants[i] > capI && plants[j] > capJ {
				counter++
				break
			}
			break
		}
		if capI < plants[i] {
			counter++
			capI = capacityA
		}
		if capJ < plants[j] {
			counter++
			capJ = capacityB
		}
		capI -= plants[i]
		capJ -= plants[j]
		i++
		j--
	}
	return counter
}