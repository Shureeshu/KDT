def test(N, K):
    # 3 ≤ N ≤ 8
    # 1 ≤ K ≤ 5
    # 지형 입력 받기
    global data, k
    k = K
    data = [list(map(int, input().split())) for _ in range(N)]
    peak_h = max(max(row) for row in data)
    peaks = []
    for i in range(N):
        for j in range(N):
            if data[i][j] == peak_h:
                peaks.append((i, j))
    rst = []
    for peak in peaks:
        i, j = peak
        visited = [(i, j)]
        rst.append(1 + max(goLeft(i, j, 0, visited), goRight(i, j, 0, visited), goUp(i, j, 0, visited), goDown(i, j, 0, visited))) 
    return max(rst)

def goLeft(i, j, z, visited):
    global data, k
    if i > 0:
        x, y = i-1, j
        if (x, y) in visited:
            return 0
        else:
            v = [(x, y)]
            v.extend(visited)
        if z < 0:
            if data[i][j] > data[x][y]:
                i, j = x, y
                return 1 + max(goLeft(i, j, z, v), goRight(i, j, z, v), goUp(i, j, z, v), goDown(i, j, z, v))
            else:
                return 0
        elif z == 0:
            if data[i][j] > data[x][y]:
                i, j = x, y
                return 1 + max(goLeft(i, j, z, v), goRight(i, j, z, v), goUp(i, j, z, v), goDown(i, j, z, v))
            elif data[x][y] - data[i][j] < k:
                i, j, z = x, y, data[x][y] - data[i][j] + 1
                return 1 + max(goLeft(i, j, z, v), goRight(i, j, z, v), goUp(i, j, z, v), goDown(i, j, z, v))
                
            else:
                return 0
        else:
            if data[i][j] - z > data[x][y]:
                i, j, z = x, y, -1
                return 1 + max(goLeft(i, j, z, v), goRight(i, j, z, v), goUp(i, j, z, v), goDown(i, j, z, v))
            else:
                return 0
    else:
        return 0
def goRight(i, j, z, visited):
    global data, k
    if i < N-1:
        x, y = i+1, j
        if (x, y) in visited:
            return 0
        else:
            v = [(x, y)]
            v.extend(visited)
        if z < 0:
            if data[i][j] > data[x][y]:
                i, j = x, y
                return 1 + max(goLeft(i, j, z, v), goRight(i, j, z, v), goUp(i, j, z, v), goDown(i, j, z, v))
                
            else:
                return 0
        
        elif z == 0:
            if data[i][j] > data[x][y]:
                i, j = x, y
                return 1 + max(goLeft(i, j, z, v), goRight(i, j, z, v), goUp(i, j, z, v), goDown(i, j, z, v))
            elif data[x][y] - data[i][j] < k:
                i, j, z = x, y, data[x][y] - data[i][j] + 1
                return 1 + max(goLeft(i, j, z, v), goRight(i, j, z, v), goUp(i, j, z, v), goDown(i, j, z, v))                
            else:
                return 0
        else:
            if data[i][j] - z > data[x][y]:
                i, j, z = x, y, -1
                return 1 + max(goLeft(i, j, z, v), goRight(i, j, z, v), goUp(i, j, z, v), goDown(i, j, z, v)) 
            else:
                return 0
    else:
        return 0
    
def goUp(i, j, z, visited):
    global data, k
    if j < N-1:
        x, y = i, j+1
        if (x, y) in visited:
            return 0
        else:
            v = [(x, y)]
            v.extend(visited)
        
        if z < 0:
            if data[i][j] > data[x][y]:
                i, j = x, y
                return 1 + max(goLeft(i, j, z, v), goRight(i, j, z, v), goUp(i, j, z, v), goDown(i, j, z, v))
            else:
                return 0
        elif z == 0:
            if data[i][j] > data[x][y]:
                i, j = x, y
                return 1 + max(goLeft(i, j, z, v), goRight(i, j, z, v), goUp(i, j, z, v), goDown(i, j, z, v))
            elif data[x][y] - data[i][j] < k:
                i, j, z = x, y, data[x][y] - data[i][j] + 1
                return 1 + max(goLeft(i, j, z, v), goRight(i, j, z, v), goUp(i, j, z, v), goDown(i, j, z, v))
            else:
                return 0
        else:
            if data[i][j] - z > data[x][y]:
                i, j, z = x, y, -1
                return 1 + max(goLeft(i, j, z, v), goRight(i, j, z, v), goUp(i, j, z, v), goDown(i, j, z, v))
            else:
                return 0
    else:
        return 0

def goDown(i, j, z, visited):
    global data, k
    if j > 0:
        x, y = i, j-1
        if (x, y) in visited:
            return 0
        else:
            v = [(x, y)]
            v.extend(visited)
        if z < 0:
            if data[i][j] > data[x][y]:
                i, j = x, y
                return 1 + max(goLeft(i, j, z, v), goRight(i, j, z, v), goUp(i, j, z, v), goDown(i, j, z, v))
            else:
                return 0
        
        elif z == 0:
            if data[i][j] > data[x][y]:
                i, j = x, y
                return 1 + max(goLeft(i, j, z, v), goRight(i, j, z, v), goUp(i, j, z, v), goDown(i, j, z, v))
            elif data[x][y] - data[i][j] < k:
                i, j, z = x, y, data[x][y] - data[i][j] + 1
                return 1 + max(goLeft(i, j, z, v), goRight(i, j, z, v), goUp(i, j, z, v), goDown(i, j, z, v))
            else:
                return 0
        else:
            if data[i][j] - z > data[x][y]:
                i, j, z = x, y, -1
                return 1 + max(goLeft(i, j, z, v), goRight(i, j, z, v), goUp(i, j, z, v), goDown(i, j, z, v))
                
            else:
                return 0
    else:
        return 0

import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
inputs = sys.stdin.readlines


T =  int(input())
rst = [0]*T
for _ in range(T):
    N, K = map(int, input().split())
    rst[_] = test(N, K)

[print(f'#{i} {rst[i-1]}') for i in range(1, len(rst)+1)]