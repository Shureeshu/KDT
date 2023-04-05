## 1204 .[S/W 문제해결 기본] 1일차 - 최빈수 구하기



# for testing
import sys
sys.stdin = open('input.txt', 'r') 

# necessary imports
from collections import Counter

# 1,000 명의 수학성적
# 최빈수를 출력하는 프로그램을 작성하여라(최빈수가 여러개 일때는 가장 큰 점수를 출력)
def getMCN(data):
    # returns the most frequent number in the data
    data = list(map(int, data.split()))
    mcn = Counter(data).most_common()
    n = 1
    v = mcn[0][1]
    while v > 1000-n*v:
        if v > mcn[n][1]:
            break
        n += 1
    return max([mcn[x][0] for x in range(0, n)])

# 테스트 케이스의 수 T
T = int(input())
for test_case in range(T):
    print(f'#{input().rstrip()} {getMCN(input())}')