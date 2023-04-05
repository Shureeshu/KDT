from collections import deque
def test(N, Lst):
    deck = deque(Lst[:-(N//2)] + list(reversed(Lst[-(N//2):])))
    new_deck = []
    for i in range(N):
        if i%2:
            new_deck.append(deck.pop())
            
        else:
            new_deck.append(deck.popleft())
            
    return ' '.join(new_deck)


import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
inputs = sys.stdin.readlines


T =  int(input())
rst = [0]*T
for _ in range(T):
    N = int(input())
    Lst = list(input().split())
    rst[_] = test(N, Lst)

[print(f'#{i} {rst[i-1]}') for i in range(1, len(rst)+1)]