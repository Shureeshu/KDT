OPENER = '([{<'
CLOSER = ')]}>'

T = 10

def s_pop(stack):
    if len(stack) > 0:
        return stack.pop()
    else:
        return -1

def test(s):
    stack = []
    for _ in s:
        if _ in OPENER:
            stack.append(OPENER.index(_))
        elif _ in CLOSER:
            if s_pop(stack) != CLOSER.index(_):
                return 0
        else:
            return 0
    if s_pop(stack) == -1:
        return 1
    else:
        return 0

# :: SWEA
'''
inputs = [input() for _ in range(T*20)]
rst = [test(x.strip()) for x in inputs[1::2]]
[print(f'#{i} {rst[i-1]}') for i in range(1, T+1)]
'''

# :: Testing

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
inputs = sys.stdin.readlines

rst = [test(x.strip()) for x in inputs()[1::2]]
for i in range(1, T + 1):
    print(f'#{i} {rst[i - 1]}')
