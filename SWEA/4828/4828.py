"""
4828: min max
"""

import sys
sys.stdin = open('4828_input.txt')


def max_min(n, numbers):
    # 최댓값, 최솟값 초기화
    max_number = numbers[0]
    min_number = numbers[0]

    # 최댓값, 최솟값을 찾아 변수에 넣음
    for i in range(n):
        if max_number < numbers[i]:
            max_number = numbers[i]
        elif numbers[i] < min_number:
            min_number = numbers[i]

    return max_number - min_number


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    n_list = list(map(int, input().split()))

    print(f'#{tc} {max_min(N, n_list)}')