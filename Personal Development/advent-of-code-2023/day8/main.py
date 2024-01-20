import sys

sys.setrecursionlimit(10000000)

def solution():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        instruction = lines[0].strip()
        lines = lines[2:]
        graph = {}
        for line in lines:
            start, end = [i.strip() for i in line.strip().split('=')]
            left, right = [i.strip() for i in end.strip().split(',')]
            left = left[1:]
            right = right[:-1]
            graph[start] = (left, right)

        def solve(node, instruction, step):
            if node == "ZZZ":
                return 1
            
            left, right = graph[node]
            if step == len(instruction):
                step = 0
            
            if instruction[step] == "L":
                return 1+solve(left, instruction, step+1)
            else:
                return 1+solve(right, instruction, step+1)
        
        return solve("AAA", instruction, 0) - 1


def solution2():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        instruction = lines[0].strip()
        lines = lines[2:]
        graph = {}
        for line in lines:
            start, end = [i.strip() for i in line.strip().split('=')]
            left, right = [i.strip() for i in end.strip().split(',')]
            left = left[1:]
            right = right[:-1]
            graph[start] = (left, right)

        def solve2(nodes, instruction, step):
            end_with_z = [i[-1]=="Z" for i in nodes]
            if all(end_with_z):
                return 1
            
            node_left, node_right = [[graph[node][0] for node in nodes], [graph[node][1] for node in nodes]]
            if step == len(instruction):
                step = 0
            
            if instruction[step] == "L":
                return 1+solve2(node_left, instruction, step+1)
            else:
                return 1+solve2(node_right, instruction, step+1)
        
        start_nodes = [node for node in graph if node[-1]=="A"]
        return solve2(start_nodes, instruction, 0) - 1



if __name__ == '__main__':
    print(solution2())