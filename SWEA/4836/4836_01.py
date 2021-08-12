# 4836. 색칠하기


def count_p(grid, color_list):
    for color in color_list:
        horizontal = color[2] - color[0] + 1
        vertical = color[3] - color[1] + 1

        x, y = color[0], color[1]

        for v in range(vertical):
            for h in range(horizontal):
                grid[x + h][y + v] += color[4]

    count = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 3:
                count += 1

    return count


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

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