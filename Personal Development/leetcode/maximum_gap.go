func maximumGap(nums []int) int {
	if len(nums) < 2 {
		return 0
	}
	sort.Ints(nums)
	var diff, maxDifference int
	for i := 0; i < len(nums)-1; i++ {
		diff = nums[i+1] - nums[i]
		if maxDifference < diff {
			maxDifference = diff
		}
	}

	return maxDifference
}