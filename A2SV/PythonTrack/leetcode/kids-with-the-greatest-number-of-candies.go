func kidsWithCandies(candies []int, extraCandies int) []bool {
    maxCandie := maximum(candies)
    ans := make([]bool, 0, len(candies))
    for _, v := range(candies){
        if v + extraCandies >= maxCandie{
            ans = append(ans, true)
        }else{
            ans = append(ans, false)
        }
    }

    return ans
}

func maximum(candies []int) int {
    currentMax := candies[0]
    for _, v := range(candies){
        currentMax = max(currentMax, v)
    }

    return currentMax
}