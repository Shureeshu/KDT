## 10505 .소득 불균형

# for testing
import sys
sys.stdin = open('input.txt', 'r') 

# necessary imports
from collections import Counter

# n명의 사람의 소득이 주어졌을 때 이 중 평균 이하의 소득을 가진 사람들의 수를 출력해야 한다.
def getBelowAvg(incomes, n):
    frq_table = Counter(incomes) # frequency table
    mean = sum([v*frq_table[v] for v in frq_table.keys()])/n
    n_low = sum([frq_table[v] for v in frq_table.keys() if v <= mean ])
    return n_low


# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 이후 T개의 테스트 케이스에 대해 각각 두 줄로 주어진다.
# 첫 번째 줄에는 정수의 개수 N 이 주어지며(1 ≤ N ≤ 10,000), 두 번째 줄에는 각 사람의 소득을 뜻하는 N개의 양의 정수가 주어진다. 이 정수들은 각각 1 이상 100,000 이하이다.

T = int(input())
for test_case in range(T):
    case_num = test_case + 1
    n = int(input())
    incomes = list(map(int, input().split()))
    print(f'#{case_num} {getBelowAvg(incomes, n)}')