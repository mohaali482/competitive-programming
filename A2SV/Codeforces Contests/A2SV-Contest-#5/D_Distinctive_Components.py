from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ca = defaultdict(list)
    for i in range(n):
        ca[a[i]].append(i)

    _min = min(a)
    nums = [i for i in (ca.keys()) if i > _min]
    ans = 0
    ans_visited = set()
    while nums:
        left = 0
        right = 0
        first = nums[-1]
        current = nums[-1]
        if current in ans_visited:
            nums.pop()
            continue
        _sum = 0
        while right < n:
            _sum += a[right]
            while _sum > current:
                if _sum in ca and _sum not in ans_visited and right - left >= 1:
                    ans_visited.add(_sum)
                    ans += len(ca[_sum])
                _sum -= a[left]
                left += 1
            
            if _sum == current and _sum not in ans_visited and right - left >= 1:
                nums.pop()
                ans_visited.add(_sum)
                ans += len(ca[_sum])
                if nums:
                    current = nums[-1]
                else:
                    break
            right += 1
        if nums and first == current:
            nums.pop()
    print(ans)