def test(dump, box):
    if len(box) <= 1:
        return 0
    L = sum(box)//len(box)
    while True:
        i = 0
        while i < len(box):
            if box[i] >= L:
                break
            else:
                i += 1
        stack = i*L - sum(box[:i])
        if stack <= dump:
            break
        else:
            L -= 1
    H = L
    while True:
        j = -1
        while j < len(box):
            if box[j] <= H:
                break
            else:
                j -= 1
        pop = sum(box[j:]) - (-j)*H
        if pop <= dump:
            break
        else:
            H += 1
    return H - L +  int(dump - pop == 0)
        





# :: SWEA
'''
inputs = [input() for _ in range(T*20)]
rst = [test(x.strip()) for x in inputs[1::2]]
[print(f'#{i} {rst[i-1]}') for i in range(1, T+1)]
'''

# :: Testing

import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
inputs = sys.stdin.readlines
T =  10 # int(input())
rst = [0]*T
for _ in range(T):
    N = int(input())
    Lst = sorted(list(map(int, input().split())))
    rst[_] = test(N, Lst)

[print(f'#{i} {rst[i-1]}') for i in range(1, len(rst)+1)]