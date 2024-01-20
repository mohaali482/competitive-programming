func mergeAlternately(word1 string, word2 string) string {
	ans := make([]byte, len(word1)+len(word2))
	i := 0
	j := 0
	pos := 0
	for i < len(word1) && j < len(word2) {
		ans[pos] = word1[i]
		ans[pos+1] = word2[j]
		i++
		j++
		pos += 2
	}
	for i < len(word1) {
		ans[pos] = word1[i]
		i++
		pos++
	}
	for j < len(word2) {
		ans[pos] = word2[j]
		j++
		pos++
	}

	return string(ans)
}