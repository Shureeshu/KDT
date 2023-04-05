# 1933  간단한 N 의 약수
N = int(input())
if N not in range(1, 1001):
    exit()
output = ''
for n in range(1, N+1):
    if not (N%n):
        output += f'{n} '
print(output.rstrip())