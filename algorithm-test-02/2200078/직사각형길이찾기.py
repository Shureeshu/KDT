## 3456 .직사각형 길이 찾기


# for testing
import sys
sys.stdin = open('input.txt', 'r') 

# necessary imports
from collections import Counter


# 직사각형의 네 변 중에서 세 변의 길이가 주어진다.
# 나머지 한 변의 길이가 얼마인지 출력하는 프로그램을 작성하라.
def getSideLen(A, B, C):
    return min(A,B,C)^2*max(A,B,C)^2//(A*B*C)
        
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 세 자연수 a, b, c(1 ≤ a, b, c ≤ 100)가 공백으로 구분되어 주어진다.
# 각 테스트 케이스마다 나머지 한 변의 길이를 출력한다.

T = int(input())
for test_case in range(T):
    case_num = test_case + 1
    a, b, c = map(int, input().split())
    print(f'#{case_num} {getSideLen(a, b, c)}')