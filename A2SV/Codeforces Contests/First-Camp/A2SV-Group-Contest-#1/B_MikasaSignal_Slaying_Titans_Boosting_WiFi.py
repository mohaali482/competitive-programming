# import sys

# input = lambda: sys.stdin.readline().strip()

# def solution():
#     e = input()
#     s = input()
#     n = [0] * 23
#     n[12] = 1
    
#     pos = 12
#     for i in e:
#         if i == "+":
#             pos+=1
#         else:
#             pos-=1

#     for i in s:
#         if i == "+":
#             j=0
#             while j < 22:
#                 if n[j]:
#                     n[j], n[j+1] = n[j+1] , n[j]
#                     j+=1
#                 j+=1
            
#         elif i == "-":
#             j=1
#             while j < 22:
#                 if n[j]:
#                     n[j], n[j-1] = n[j-1] , n[j]
#                     j+=1
#                 j+=1
            
#         else:
#             j=0
#             while j < 22:
#                 if n[j]:
#                     n[j+1] += n[j]/2
#                     n[j-1] += n[j]/2
#                     n[j] = 0
#                     j+=1
#                 j+=1
    
#     return "%.12f"%n[pos]


# print(solution())




import sys
 
input = lambda: sys.stdin.readline().strip()
 
def solution():
    e = input()
    s = input()
    n = [0] * 23
    def find(pos, prev, curr):
        print(n)
        if pos == len(s):
            return
        if s[pos] == "+":
            n[prev] = 0
            n[prev+1] += curr
            find(pos+1, prev+1, curr)
        elif s[pos] == "-":
            n[prev] = 0
            n[prev-1] += curr
            find(pos+1, prev-1, curr)
        else:
            n[prev] = 0
            curr /= 2
            n[prev+1] += curr
            find(pos+1, prev+1, curr)
            n[prev-1] += curr
            find(pos+1, prev-1, curr)
    
    position = 12
    for i in e:
        if i == "+":
            position += 1
        else:
            position -= 1
    n[12] = 1
    find(0, 12, 1)
    return "%.12f" % round(n[position], 9)
        
print(solution())
