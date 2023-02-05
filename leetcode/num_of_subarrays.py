class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i = 0
        j = k
        counter = 0
        threshold = k * threshold
        summation = sum(arr[i:j])
        maxim = len(arr) - (k-1)
        if summation >= threshold:
            counter += 1
        while j < len(arr):
            summation = summation - arr[i] + arr[j]
            if summation >= threshold:
                counter += 1
            i += 1
            j += 1

        return counter
