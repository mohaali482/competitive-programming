func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	st := []rune(strconv.Itoa(x))
	n := len(st) - 1
	for i, j := 0, n; i < j; i, j = i+1, j-1 {
		if st[i] != st[j] {
			return false
		}
	}

	return true
}