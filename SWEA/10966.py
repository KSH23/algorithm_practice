# 10966. 물놀이를 가자


from collections import deque


def bfs():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while len(q) > 0:
        cur = q.popleft()
        cur_r, cur_c = cur[0], cur[1]

        for d in range(4):
            nr, nc = cur_r + dr[d], cur_c + dc[d]
            if nr < 0 or nc < 0 or row <= nr or col <= nc:
                continue
            if visited[nr][nc] > -1:
                continue

            q.append((nr, nc))
            visited[nr][nc] = visited[cur_r][cur_c] + 1


T = int(input())
for tc in range(1, T+1):
    row, col = map(int, input().split())
    MAP = [list(input()) for _ in range(row)]

    visited = [[-1] * col for _ in range(row)]
    q = deque()
    for i in range(row):
        for j in range(col):
            if MAP[i][j] == 'W':
                q.append((i, j))
                visited[i][j] = 0

    bfs()
    ans = 0
    for i in range(row):
        for j in range(col):
            if MAP[i][j] == 'L':
                ans += visited[i][j]

    print(f'#{tc} {ans}')