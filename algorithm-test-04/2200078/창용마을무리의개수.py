from collections import deque
def test(V, E):
    global graph
    graph = [{_, } for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[b].add(a)
        graph[a].add(b)
    cnt = 0
    v = list(range(1, V+1))
    while v:
        start = v.pop()
        if graph[start]:
            getGroup(start)
            cnt += 1
    return cnt
def getGroup(start):
    global graph
    stack = [start]
    while stack:
        a = stack.pop()
        while graph[a]:
            for b in graph[a]:
                stack.append(b)
            graph[a].clear()


import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
inputs = sys.stdin.readlines


T =  int(input())
rst = [0]*T
for _ in range(T):
    N, M = map(int, input().split())
    rst[_] = test(N, M)

[print(f'#{i} {rst[i-1]}') for i in range(1, len(rst)+1)]