func countPrimes(n int) int {
	if n == 0 {
		return 0
	} else if n == 1 {
		return 0
	} else if n == 2 {
		return 0
	} else if n == 3 {
		return 1
	}
	prime := make([]bool, n)
	prime[0] = true
	prime[1] = true
	var i, j int
	for i = 2; i < int(math.Pow(float64(n), 0.5)+1); i++ {
		if !prime[i] {
			for j = i + i; j < n; j += i {
				prime[j] = true
			}
		}
	}

	var count int = 0
	for i := 2; i < n; i++ {
		if !prime[i] {
			count++
		}
	}

	return count
}