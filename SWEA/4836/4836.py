"""
4836: 색칠하기
"""

import sys
sys.stdin = open('4836_input.txt')


def count_p(grid, color_list):
    # 주어진 색칠 리스트들을 하나씩 돌면서 
    # 그리드에 주어진 색상 값을 넣을 예정
    for color in color_list:
        # 칠할 범위의 가로, 세로 길이를 구함
        horizontal = color[2] - color[0] + 1
        vertical = color[3] - color[1] + 1

        # 칠할 범위의 기준점 설정
        x, y = color[0], color[1]

        # 기준점을 중심으로 색칠
        for v in range(vertical):
            for h in range(horizontal):
                grid[x + h][y + v] += color[4]
       
    # 완성된 그리드에서 보라색(3)을 세고 그 값을 반환
    count = 0
    for i in range(10):
        count += grid[i].count(3)

    return count


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 0으로만 채워진 2차원 배열로 색칠할 10x10 격자 생성
    my_grid = []
    for i in range(10):
        my_grid_line = []
        for j in range(10):
            my_grid_line.append(0)
        my_grid.append(my_grid_line)

    my_color = []
    for n in range(N):
        my_color.append(list(map(int, input().split())))

    print(f'#{tc} {count_p(my_grid, my_color)}')