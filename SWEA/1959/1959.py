"""
1959: 두 개의 숫자열
"""

import sys
sys.stdin = open('1959_input.txt')


# 두 개의 리스트를 받아 결과 값을 출력하는 함수
def find_max(list1, list2):
    short_list = []
    long_list = []

    # 길이에 따른 리스트 구분 -> 긴 리스트는 바깥 for문, 짧은 리스트는 안쪽 for문으로
    if len(list1) >= len(list2):
        long_list, short_list = list1, list2
    else:
        long_list, short_list = list2, list1

    result = 0   # value 값 중 최댓값을 담음
    value = 0   # 한 번의 계산 결과를 담음

    # 이중 for문을 돌며 가능한 경우를 모두 계산
    for i in range(len(long_list) - len(short_list) + 1):
        for j in range(len(short_list)):
            # print(f'i+j: {i+j}, j: {j}, short_list[j]: {short_list[j]}, long_list[i+j]: {long_list[i+j]}')
            value += short_list[j] * long_list[i+j]
        # print(f'value: {value}')
        if value > result:
            result = value   # 최댓값을 result에 저장
        value = 0   # 다음 계산을 위해 value 초기화
    
    return result


T = int(input())

for tc in range(1, T+1):
    len1, len2 =  map(int, input().split())

    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))

    print(f'#{tc} {find_max(list1, list2)}')