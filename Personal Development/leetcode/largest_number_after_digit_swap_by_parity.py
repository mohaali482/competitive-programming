class Solution:
    def largestInteger(self, num: int) -> int:
        odd_num = []
        even_num = []
        for i in str(num):
            if int(i) % 2 == 0:
                heapq.heappush(even_num, i)
            else:
                heapq.heappush(odd_num, i)
        new_num = ""
        for i in str(num)[::-1]:
            if int(i) % 2 == 0:
                new_num += heapq.heappop(even_num)
            else:
                new_num += heapq.heappop(odd_num)

        return int(new_num[::-1])
