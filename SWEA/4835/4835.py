"""
4835: 구간합
"""

import sys
sys.stdin = open('4835_input.txt')


def max_min_sum(m, num_list):
    # 최댓값, 최솟값을 맨 첫번째 경우로 설정
    max_sum = min_sum = sum(num_list[0: m])

    # 리스트를 한 칸씩 전진해 기준점을 잡음
    for main_idx in range(len(num_list) - m + 1):
        temp_sum = 0
        
        # 기준점에서 m칸의 숫자를 더한 후 최댓값 또는 최솟값을 갱신
        for idx in range(main_idx, main_idx + m):
            temp_sum += num_list[idx]
        if max_sum < temp_sum:
            max_sum = temp_sum
        elif temp_sum < min_sum:
            min_sum = temp_sum
        # print(f'max_sum: {max_sum}, min_sum: {min_sum}, temp_sum: {temp_sum}')
        
    return max_sum - min_sum


T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    my_list = list(map(int, input().split()))

    print(f'#{tc} {max_min_sum(M, my_list)}')