"""
4843: 특별한 정렬
"""

import sys
sys.stdin = open('4843_input.txt')


def special_sort(n, num_list):
    result = []    # 결과를 담을 변수 생성

    # 총 5번을 돌며 원하는 값을 result에 할당
    for i in range(5):
        max_num = min_num = num_list[0]    # 최대, 최소값 초기화

        # 주어진 숫자 리스트를 전부 돌며 최대, 최소값을 찾음
        for num in num_list:
            if num > max_num:
                max_num = num
            elif num < min_num:
                min_num = num
        
        # 찾은 최대, 최소값을 각각 result에 넣고 기존 리스트에서 삭제
        result.extend([max_num, min_num])
        num_list.remove(max_num)
        num_list.remove(min_num)

    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    my_list = list(map(int, input().split()))
    
    result_list = ' '.join(map(str, special_sort(N, my_list)))
    print(f'#{tc} {result_list}')