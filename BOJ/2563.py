# 2563. 색종이


def paper_area(paper):
    count = 0    # 영역을 세는 변수
    grid = []    # 100x100 크기의 도화지

    # 도화지를 모두 0으로 채움
    for i in range(100):
        temp_grid = []
        for j in range(100):
            temp_grid.append(0)
        grid.append(temp_grid)

    # 각 좌표를 돌며 색종이가 붙으면 1로 바꿔주고 영역을 셈
    for p in paper:
        for i in range(p[1], p[1] + 10):
            for j in range(p[0], p[0] + 10):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    count += 1

    return count


N = int(input())

my_paper = []
for i in range(N):
    my_paper.append(list(map(int, input().split())))

print(paper_area(my_paper))