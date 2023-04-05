def test(N, K):
    Lst = list(map(int, input().split()))
    x = [0]*(N+1)
    for _ in range(K):
        x[Lst[_]] = 1
    rst = ' '.join([str(i) for i in range(1, N+1) if x[i] == 0])
    return rst

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
