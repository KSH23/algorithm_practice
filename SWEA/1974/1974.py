"""
1974: 스도쿠 검증
"""

import sys
sys.stdin = open('1974_input.txt')


def check_sudoku(sudoku):
    # 가로 줄 확인
    for v in range(9):  
        temp_list = []    # 확인을 위해 한 줄 씩 임시 리스트에 담음
        for h in range(9):
            temp_list += [sudoku[v][h]]

        # print(temp_list)
        # print(list(set(temp_list)))
        # 임시 리스트를 set으로 만들어 중복된 요소를 없애고 길이를 측정
        # 길이가 9가 아니라면 바로 0 리턴
        if len(list(set(temp_list))) != 9:
            return 0


    # 세로 줄 확인
    for h in range(9):    
        temp_list = []
        for v in range(9):
            temp_list += [sudoku[v][h]]
        if len(list(set(temp_list))) != 9:
            return 0


    # 3x3 확인
    # 각 3x3 정사각형의 좌측 상단을 중심으로 잡음
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp_list = []

            # 중심에서부터 우측 하단을 향해서 감
            for k in range(3):
                for l in range(3):
                    temp_list += [sudoku[i+k][j+l]]
            if len(list(set(temp_list))) != 9:
                return 0
                
    # 아무 문제 없다면 1을 반환
    return 1


T = int(input())

for tc in range(1, T+1):
    my_sudoku = []
    for i in range(9):
        my_sudoku.append(list(map(int, input().split())))

    # print(my_sudoku)
    print(f'#{tc} {check_sudoku(my_sudoku)}')
    