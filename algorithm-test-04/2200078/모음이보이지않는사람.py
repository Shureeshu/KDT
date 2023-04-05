def test(S):
    rst = ''
    for chr in S:
        if chr not in 'aeiou':
            rst += chr
    return rst


import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
inputs = sys.stdin.readlines


T =  int(input())
rst = [0]*T
for _ in range(T):
    S = input().strip()
    rst[_] = test(S)

[print(f'#{i} {rst[i-1]}') for i in range(1, len(rst)+1)]