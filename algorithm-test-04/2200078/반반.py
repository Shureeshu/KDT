from collections import deque
def test(S):
    S = [S[i] for i in range(4)]
    if len(set(S)) == 2:
        for chr in set(S):
            if S.count(chr) != 2:
                return "No"
        return "Yes"
    else:
        return "No"


import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
inputs = sys.stdin.readlines


T = int(input())
rst = [0]*T
for _ in range(T):
    S = input()
    # Lst = list(input().split())
    rst[_] = test(S)

[print(f'#{i} {rst[i-1]}') for i in range(1, len(rst)+1)]