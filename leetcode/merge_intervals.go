import "sort"

func merge(intervals [][]int) [][]int {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
	ans := make([][]int, 0)
	temp := intervals[0]
	for i := 1; i < len(intervals); i++ {
		if temp[0] <= intervals[i][0] && intervals[i][0] <= temp[1] {
			if temp[1] < intervals[i][1] {
				temp[1] = intervals[i][1]
			}
		} else {
			ans = append(ans, temp)
			temp = intervals[i]
		}
	}
	ans = append(ans, temp)
	return ans
}