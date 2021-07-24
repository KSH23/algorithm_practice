"""
1961: 숫자 배열 회전
"""

import sys
sys.stdin = open('1961_input.txt')


# 90도 회전 출력 함수
def rotate_90(matrix_list):
    result = []    # 회전 결과를 리스트 안에 리스트로 묶어서 저장할 예정

    for h in range(len(matrix_list[0])):
        lines = ''    # 한 줄의 회전 결과를 str으로 변환하여 저장

        # 좌측 하단에서 시작해 아래서 위로 움직이며 이후 행을 바꾼 뒤 반복
        for v in range(len(matrix_list) - 1, -1, -1):
            lines += str(matrix_list[v][h])
        result += [lines]    # 한 줄의 변환 결과를 미리 만들어둔 리스트에 저장

    return result


# 180도 회전 출력 함수
def rotate_180(matrix_list):
    result = []

    for v in range(len(matrix_list) - 1, -1, -1):
        lines = ''

        # 우측 하단에서 시작해 왼쪽으로 움직이며 이후 열을 바꾼 뒤 반복
        for h in range(len(matrix_list[0]) - 1, -1, -1):
            lines += str(matrix_list[v][h])
        result += [lines]

    return result


# 270도 회전 출력 함수
def rotate_270(matrix_list):
    result = []

    for h in range(len(matrix_list[0]) - 1, -1, -1):
        lines = ''

        # 우측 상단에서 시작해 아래로 움직이며 이후 행을 바꾼 뒤 반복
        for v in range(len(matrix_list)):
            lines += str(matrix_list[v][h])
        result += [lines]

    return result


# 세 개의 크기가 같은 리스트를 받아 같은 인덱스 값끼리 반환하는 함수
def same_idx(list1, list2, list3, index):
    total_list = f'{list1[index]} {list2[index]} {list3[index]}'

    return total_list


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    matrix = []
    
    for i in range(n):
        matrix.append(list(map(int, input().split())))

    # print(array)
    # print(rotate_90(matrix))
    # print(rotate_180(matrix))
    # print(rotate_270(matrix))
    # print(print_rotation(rotate_90(matrix), rotate_180(matrix), rotate_270(matrix), 1))

    print(f'#{tc}')
    for i in range(n):
        print(same_idx(rotate_90(matrix), rotate_180(matrix), rotate_270(matrix), i))