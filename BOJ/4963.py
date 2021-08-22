# 4963. 섬의 개수


import sys
sys.setrecursionlimit(100000)


def dfs(i, j):
    di = [-1, -1, 0, 1, 1, 1, 0, -1]    # 시계방향으로 12시부터 순서대로
    dj = [0, 1, 1, 1, 0, -1, -1, -1]

    for k in range(8):
        if i + di[k] >= h or i + di[k] < 0 or j + dj[k] >= w or j + dj[k] < 0:
            continue
        if MAP[i + di[k]][j + dj[k]] == 0 or visited[i + di[k]][j + dj[k]] == 1:
            continue

        next_r = i + di[k]
        next_c = j + dj[k]
        visited[next_r][next_c] = 1
        dfs(next_r, next_c)


while True:
    w, h = map(int, input().split())

    if w == 0:
        break

    MAP = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    ans = 0
    for i in range(h):
        for j in range(w):
            if MAP[i][j] == 0 or visited[i][j] == 1:
                continue
            visited[i][j] = 1
            dfs(i, j)
            ans += 1

    print(ans)