"""
1970: 쉬운 거스름돈
"""

import sys
sys.stdin = open('1970_input.txt')


# 지폐 dict를 받아 갯수 list를 반환하는 함수
def give_change(money_dict, change):
    for money in list(money_dict.keys()):
        if change >= money:
            money_dict[money] = change // money
            change = change % money
    
    return list(money_dict.values())


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    
    # 지폐 dict
    money_dict = {50000: 0, 10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0, 50: 0, 10: 0}

    # 지폐 갯수 list
    result = give_change(money_dict, n)

    print(f'#{tc}')

    # 맨 마지막 요소만 빼고 출력
    for i in range(len(result) - 1):
        print(result[i], end=' ')

    # 맨 마지막 요소는 뒤에 띄어쓰기 없이 출력
    print(result[-1])