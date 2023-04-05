# 2072  홀수만 더하기
# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.
# N in I, 0<=N<=10000
output = ''
T = int(input())
for t in range(1, T+1):
    output += f'#{t} '
    x = list(map(int, input().split()))
    y = 0
    for xi in x:
        y += xi*(xi%2)
    output += f'{y}'
    output += f'\n'
print(output.rstrip())