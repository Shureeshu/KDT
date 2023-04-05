## 14649 .신용카드 만들기 1

# for testing
import sys
sys.stdin = open('input.txt', 'r') 

# necessary imports
from collections import Counter

# 신용카드 번호는 룬 공식(LUHN Formula)을 만족해야합니다.
# 룬 공식이란 카드 번호에서 마지막 자리(열여섯번째) 숫자N을 구하는 공식입니다.

# 1) 매 홀수자리의 숫자마다 2를 곱해서 더합니다. 
# 2) 매 짝수자리의 숫자는 그대로 더합니다.
# 3) 1)과 2)를 더 한 숫자에 N을 더 한 숫자가 10으로 나눴을 때 나눠 떨어지면 유효한 숫자입니다. 

# 16자리의 카드 번호 중 처음 15개가 주어졌을 때 룬 공식을 만족하기 위해 마지막에 들어가야하는 숫자N을 구하는 프로그램을 작성하시오.
def getN(numbers):
    num15 = list(map(int, numbers.split())) 
    n = 0
    for i in range(0, 15):
        n += int(num15[i])*(2-i%2)
    n16 = (10-(n%10))%10
    return n16

 
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스는 한 개의 줄로 이루어지며, 각 줄에는 공백으로 구분한 자연수 15개가 주어진다. 
# 각 테스트 케이스마다, 룬 공식 유효성 검사를 통과하기 위해 16번째 자리에 들어갸아하는 숫자를 찾아서 출력한다.
T = int(input())
for test_case in range(T):
    case_num = test_case + 1
    numbers = input()
    print(f'#{case_num} {getN(numbers)}')
 