class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = {}
        for i in nums:
            if not i in a:
                a[i]=[]
 
            if i+1 in a:
                a[i].append(i+1)
                a[i+1].append(i)
 
            if i-1 in a:
                a[i].append(i-1)
                a[i-1].append(i)
 
        keys = set(a.keys())
        max_val = 0
        while keys:
            key = keys.pop()
            st = [key]
            counter = 1
 
            while st:
                cu_key = st.pop()
                children = a[cu_key]
                for i in children:
                    if i in keys:
                        st.append(i)
                        counter += 1
                        keys.remove(i)
 
            max_val = max(counter, max_val)
        return max_val