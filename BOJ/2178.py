# 2178. 미로 탐색


row, col = map(int, input().split())
MAP = [list(map(int, input())) for _ in range(row)]
visited = [[0] * col for _ in range(row)]
visited[0][0] = 1

Q = [(0, 0)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

while len(Q) > 0:
    now = Q.pop(0)
    now_r, now_c = now[0], now[1]

    for k in range(4):
        nr, nc = now_r + di[k], now_c + dj[k]

        if nr < 0 or nc < 0 or row <= nr or col <= nc:
            continue
        if visited[nr][nc] > 0 or MAP[nr][nc] == 0:
            continue
        Q.append((nr, nc))
        visited[nr][nc] = visited[now_r][now_c] + 1

print(visited[row-1][col-1])