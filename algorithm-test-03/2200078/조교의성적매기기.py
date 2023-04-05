def score(s):
    Lst = list(map(int, s.split()))
    weight = [35, 45, 20]
    return sum(x*y for x, y in zip(Lst, weight))

def test(N, K):
    GRADE = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    scores = [score(input()) for _ in range(N)]
    rank = 1+sum(1 for x in scores if x > scores[K-1])
    return GRADE[(10*rank-1)//N]



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
