"""
4834: 숫자 카드
"""

import sys
sys.stdin = open('4834_input.txt')


def count_card(num_list):
    # 카드와 그 갯수를 담는 dict 생성
    num_dict = {}    
    for num in num_list:
        num_dict[num] = num_list.count(num)

    # 최대 카드 갯수와 이에 해당하는 카드들을 담는 리스트 생성
    max_val = 0
    max_key = []
    for key, val in num_dict.items():
        if val >= max_val:
            max_val = val
            max_key.append(key)

    result = str(max(max_key)) + ' ' + str(max_val)

    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    my_list = list(map(int, input()))

    print(f'#{tc} {count_card(my_list)}')

