# 1288  새로운 불면증 치료법
# N의 배수 번호인 양을 세기로 하였다.
output = ''
T = int(input())
for t in range(1, T+1):
    output += f'#{t} '
    N = int(input())
    if N not in range(1, 1000001):
        exit()
    S = set()
    x = 1
    while len(S) < 10:
        for i in str(x*N):
            S.add(i)
        x += 1
    output += f'{(x-1)*N}\n'
print(output.rstrip())