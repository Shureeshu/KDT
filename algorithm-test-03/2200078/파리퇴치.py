def get_x(arr, v):
    s = sum(sum(arr[i][j] for i in range(v[0], v[0]+M) if i < N) for j in range(v[1], v[1]+M) if j < N)
    return s

def test(N, M):
    arr = [list(map(int, input().split())) for _ in range(N)]
    x = max(max(get_x(arr, (i, j)) for j in range(N)) for i in range(N))
    return x

# :: Testing
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
inputs = sys.stdin.readlines


T = int(input())
rst = [0]*T
for _ in range(T):
    N, M = map(int, input().split())
    rst[_] = test(N, M)

[print(f'#{i} {rst[i-1]}') for i in range(1, len(rst)+1)]
