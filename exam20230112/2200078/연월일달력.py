# 2056  연월일 달력
# 해당 날짜의 유효성을 판단한 후,
# 날짜가 유효하다면 ”YYYY/MM/DD”형식으로 출력하고,
# 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.
output = ''
check = dict()
for mm in ('01', '03', '05', '07', '08', '10', '12'):
    check.update({mm: 31})
for mm in ('04', '06', '09', '11'):
    check.update({mm: 30})
check.update({'02': 28})
T = int(input())
for t in range(1, T+1):
    output += f'#{t} '
    date = input()
    yyyy, mm, dd = date[:4], date[4:6], date[6:]
    if mm in check.keys():
        if (int(dd)-1) in range(0,check[mm]):
            output += f'{yyyy}/{mm}/{dd}\n'
        else:
            output += f'-1\n'
    else:
            output += f'-1\n'
print(output.rstrip())