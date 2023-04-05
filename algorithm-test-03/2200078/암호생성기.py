# import sys

# from math import log, floor
# from random import randint, choice
# from time import time
# from collections import deque

# sys.setrecursionlimit(100000000)
# sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
# inputs = sys.stdin.readlines

def test(s):
    n = list(map(int, s.split()))
    while min(n) > 15:
        n = [x-15 for x in n]
    while True:
        for i in range(5):
            n[i] = max(0, n[i]-i-1)
            if n[i] == 0:
                return n[i+1:]+n[:i+1]
        n = n[i+1:]+n[:i+1]


# :: SWEA
'''
T = 10
inputs = [input() for _ in range(T*2)]
rst = [test(x.strip()) for x in inputs[1::2]]
[print(f'#{i} '+ ' '.join(str(n) for n in rst[i-1])) for i in range(1, len(rst)+1)]
'''

# :: Testing

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
inputs = sys.stdin.readlines

rst = [test(x.strip()) for x in inputs()[1::2]]
[print(f'#{i} '+ ' '.join(str(n) for n in rst[i-1])) for i in range(1, len(rst)+1)]
