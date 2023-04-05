## 14654 .신용카드 만들기 2

# for testing
import sys
sys.stdin = open('input.txt', 'r') 

# necessary imports
from collections import Counter

# 1. 카드 번호는 3, 4, 5, 6, 9 로 시작해야 한다.
# 2. 카드 번호에 "-"이 들어갈 수 있으며 "-" 를 제외한 숫자의 개수는 16개이다.
# EX) 6471-6836-9525-5276
# EX) 3029192045012901

# 카드 번호가 주어졌을 때 해당 번호로 신용카드를 만들 수 있는지 판별하는 프로그램을 작성하시오.
def isValid(numbers):
    numbers = numbers.lstrip('-')
    c1 = numbers[0] in '34569'
    c2 = (len(numbers)-numbers.count('-') == 16)
    return c1*c2

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스는 한 개의 줄로 이루어지며, 각 줄에는 공백으로 구분한 자연수 15개가 주어진다. 
# 각 테스트 케이스마다, 룬 공식 유효성 검사를 통과하기 위해 16번째 자리에 들어갸아하는 숫자를 찾아서 출력한다.
T = int(input())
for test_case in range(T):
    case_num = test_case + 1
    numbers = input()
    print(f'#{case_num} {isValid(numbers)}')
 