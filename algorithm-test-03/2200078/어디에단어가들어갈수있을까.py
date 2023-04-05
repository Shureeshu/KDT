def test(N, K):
    matrix = [list(map(int, input().split())) for i in range(N)]
    t_matrix = [[x[i] for x in matrix] for i in range(N)]
    
    for x in matrix:
        for i in range(1, N):
            if x[i] == 1:
                x[i], x[i-1] = x[i]+x[i-1], 0

    for x in t_matrix:
        for i in range(1, N):
            if x[i] == 1:
                x[i], x[i-1] = x[i]+x[i-1], 0
    
    cnt = sum(x.count(K)+y.count(K) for x, y in zip(matrix, t_matrix))
    return cnt
    
# :: Testing
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
inputs = sys.stdin.readlines


T = int(input())
rst = [0]*T
for _ in range(T):
    N, K = map(int, input().split())
    rst[_] = test(N, K)

[print(f'#{i} {rst[i-1]}') for i in range(1, len(rst)+1)]
