func reductionOperations(nums []int) int {
    slices.Sort(nums)
    ans := 0
    num := nums[len(nums)-1]
    window := 0
    window2 := 0
    for i := len(nums)-1; i > -1; i--{
        if nums[i] == num{
            window++
        }else{
            window2 += window
            ans += window2
            window = 1
            num = nums[i]
        }
    }
    return ans
}