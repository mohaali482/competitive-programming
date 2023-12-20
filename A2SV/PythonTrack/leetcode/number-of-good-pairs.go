func numIdenticalPairs(nums []int) int {
    count := make(map[int]int)
    for _, num := range(nums){
        if _, ok := count[num]; ok{
            count[num]++
        }else{
            count[num] = 1
        }
    }
    ans := 0
    for _, value := range(count){
        if value < 2{
            continue
        }
        ans += combination(value, 2)
    }

    return ans
}

func combination(n, k int) int {
    if n < 0 || k < 0 {
		return 0
	}
	if n < k {
		return 0
	}
	if k > n/2 {
		k = n - k
	}
	b := 1
	for i := 1; i <= k; i++ {
		b = (n - k + i) * b / i
	}
	return b
}