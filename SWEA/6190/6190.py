"""
6190: 정곤이의 단조 증가하는 수
"""

import sys
from typing import Tuple
sys.stdin = open('6190_input.txt')


def increasing_num(n, num_list):
    temp = 0    # A_i X A_j 값을 구한 후 임시 변수에 저장
    
    temp_list = []    # A_i X A_j 값들을 저장할 리스트
    
    # 이중 for문으로 모든 경우의 값을 리스트에 넣음
    for i in range(n - 1):
        for j in range(i+1, n):
            temp = num_list[i] * num_list[j]
            temp_list.append(temp)

    # 리스트를 내림차순으로 정렬함
    # 최댓값을 발견하면 더 계산 안하고 바로 return하기 위함
    temp_list.sort(reverse=True)

    # 모든 요소를 돌며 단조 증가하는 수인지 확인
    for t in temp_list:
        if is_increasing(t) == True:
            return t

    return -1


def is_increasing(number):
    while True:
        # 숫자가 일의 자리밖에 없다면 맞다
        if number < 10:
            return True
        
        # 숫자가 두 자리 수일 때
        elif number < 100 and number // 10 <= number % 10:
            return True

        # 그 외의 경우
        elif number // 10 % 10  <= number % 10:
                number = number // 10
        
        # 하나도 해당되지 않는다면 이 숫자는 아니다
        else:
            return False


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    my_list = list(map(int, input().split()))

    print(f'#{tc} {increasing_num(N, my_list)}')