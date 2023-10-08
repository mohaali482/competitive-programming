/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func insertionSortList(head *ListNode) *ListNode {
	if head.Next == nil {
		return head
	}
	ints := make([]int, 0)
	for head != nil {
		ints = append(ints, head.Val)
		head = head.Next
	}
	sort.Ints(ints)
	ans := new(ListNode)
	ite := ans
	for i := 0; i < len(ints); i++ {
		ite.Val = ints[i]
		if i+1 < len(ints) {
			ite.Next = &ListNode{}
			ite = ite.Next
		}
	}
	return ans

}
