# 4875. 미로


def dfs(row, col):
    di = [-1, 1, 0, 0]  # 상하좌우
    dj = [0, 0, -1, 1]  # 상하좌우

    visited[row][col] = 1

    if MAP[row][col] == 3:
        return 1

    for k in range(4):
        if row + di[k] >= N or col + dj[k] >= N or row + di[k] < 0 or col + dj[k] < 0:
            continue
        if MAP[row + di[k]][col + dj[k]] == 1:
            continue
        if visited[row + di[k]][col + dj[k]] == 1:
            continue
        if dfs(row + di[k], col + dj[k]):
            return 1

    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().rstrip())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 2:
                print('#{} {}'.format(tc, dfs(i, j)))
                break