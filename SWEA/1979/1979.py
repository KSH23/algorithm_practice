"""
1979: 어디에 단어가 들어갈 수 있을까
"""

import sys
sys.stdin = open('1979_input.txt')


# 연속된 가로 흰 줄 길이를 구해 리스트에 담아 반환하는 함수
def find_horizontal_white(space, word_length):
    horizontal_line = []    # 연속적인 white의 갯수를 세다가 0을 만나면 여기에 저장
    line = 0    # 연속된 white의 수를 세는 변수

    # 주어진 공간을 전부 도는 for문
    for ver in range(len(space)):
        for hor in range(len(space[0])):
            if space[ver][hor] == 1:
                line += 1    # white를 발견하면 line에 1을 더함
                # print(f'space[ver][hor]: {space[ver][hor]}, line: {line}')
            else:    # black(0)을 만나는 경우
                horizontal_line += [line]    # black을 만나면 즉시 연속된 white의 갯수를 list에 담고
                line = 0    # 연속된 white가 끝났기 때문에 다시 line을 0으로 초기화
        horizontal_line += [line]    # 가로 한 줄이 끝나면 무조건 list에 담은 후
        line = 0    # 가로 한 줄이 끝났기 때문에 line도 0으로 초기화

    result = 0    # 위에서 구한 list에 원하는 숫자가 몇 번 들어있는지 세기 위한 변수
    for i in range(len(horizontal_line)):
        if horizontal_line[i] == word_length: 
            result += 1
            
    return result 


# 연속된 세로 흰 줄 길이를 구해 리스트에 담아 반환하는 함수
# 논리는 위 함수와 동일
def find_vertical_white(space, word_length):
    vertical_line = []
    line = 0
    for hor in range(len(space[0])):
        for ver in range(len(space)):
            if space[ver][hor] == 1:
                line += 1
            else:
                vertical_line += [line]
                line = 0
        vertical_line += [line]
        line = 0

    result = 0
    for i in range(len(vertical_line)):
        if vertical_line[i] == word_length:
            result += 1
            
    return result 


T = int(input())

for tc in range(1, T+1):
    n, k =  map(int, input().split())
    puzzle = []

    for i in range(n):
        puzzle.append(list(map(int, input().split())))

    # print(puzzle)
    # print(find_horizontal_white(puzzle, k))
    # print(find_vertical_white(puzzle, k))

    print(f'#{tc} {find_horizontal_white(puzzle, k) + find_vertical_white(puzzle, k)}')
