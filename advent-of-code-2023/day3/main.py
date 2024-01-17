from collections import defaultdict
from typing import List

movement = [
    [0, 1],
    [0, -1],
    [1, 0],
    [1, 1],
    [1, -1],
    [-1, 0],
    [-1, 1],
    [-1, -1],
]

def valid(lines, point):
    if point[0] < 0 or point[0] >= len(lines):
        return False
    if point[1] < 0 or point[1] >= len(lines[0]):
        return False
    
    return True

def check(lines: List[List[str]], i: int, j: int):
    for x, y in movement:
        if valid(lines, [i + x, j + y]):
            if not lines[i + x][j + y].isdigit() and lines[i + x][j + y] != ".":
                return [True, lines[i + x][j + y]=="*", (i+x, j+y)]
    return [False, False, (0,0)]

def solution(lines: List[List[str]]):
    total = 0
    nums = defaultdict(list)
    for i in range(len(lines)):
        num = ""
        found = False
        star = False
        star_ind = (-1, -1)
        for j in range(len(lines[i])):
            if lines[i][j].isdigit():
                num += lines[i][j]
                if not found:
                    found, star, star_ind = check(lines, i, j)
            else:
                if found:
                    total += int(num)
                    if star:
                        nums[star_ind].append(int(num))
                num = ""
                found = False
        if found:
            total += int(num)
            if star:
                nums[star_ind].append(int(num))
        

    _sum = 0
    for v in nums.values():
        c = 1
        if len(v) == 2:
            for i in v:
                total -= i
                c *= i
            _sum += c
        else:
            total -= v[0]
                
    
    return _sum
            

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        print(solution(lines))