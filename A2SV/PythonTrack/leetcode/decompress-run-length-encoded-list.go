func decompressRLElist(nums []int) []int {
    size := 0
    for i := 0; i < len(nums); i+=2{
        size += nums[i]
    }
    ans := make([]int, 0, size)
    for i := 0; i < len(nums); i+= 2{
        for j := 0; j < nums[i]; j++{
            ans = append(ans, nums[i+1])
        }
    }

    return ans
}