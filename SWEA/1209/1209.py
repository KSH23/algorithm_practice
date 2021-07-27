"""
1209: Sum
"""

import sys
sys.stdin = open('1209_input.txt')


def find_max(matrix):
    true_max = 0    # 최종 가장 큰 값

    for i in range(100):
        h_max = 0    # 가로 줄의 합
        v_max = 0    # 세로 줄의 합
        for j in range(100):
            h_max += matrix[i][j]
            v_max += matrix[j][i]
        
        # 가로 / 세로 줄의 합 중 최댓값이 나오면 갱신
        if h_max > true_max:
            true_max = h_max
        if v_max > true_max:
            true_max = v_max

        # 대각선 두 줄의 합
        d_max = 0
        rd_max = 0
        d_max += matrix[i][i]
        rd_max += matrix[i][len(matrix) - 1 - i]

    # 대각선 줄에서 최댓값이 나오면 갱신
    if d_max > true_max:
        true_max = d_max  
    if rd_max > true_max:
        true_max = rd_max

    return true_max


T = 10

for tc in range(1, T+1):
    test_number = int(input())
    my_matrix = []

    # input 값으로 2차원 배열 만들기
    for i in range(100):
        my_matrix.append(list(map(int, input().split())))

    print(f'#{tc} {find_max(my_matrix)}')

    