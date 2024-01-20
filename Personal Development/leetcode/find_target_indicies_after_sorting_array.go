func targetIndices(nums []int, target int) []int {
	ans := make([]int, 0)
	sort.Ints(nums)
	for ind, val := range nums {
		if val == target {
			ans = append(ans, ind)
		}
	}
	return ans

}