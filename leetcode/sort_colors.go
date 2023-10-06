func sortColors(nums []int) {
	var key, j int

	for i := 1; i < len(nums); i++ {
		key = nums[i]
		j = i - 1
		for j >= 0 && key < nums[j] {
			nums[j+1] = nums[j]
			j -= 1
		}
		nums[j+1] = key
	}

}