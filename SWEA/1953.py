# 1953. 탈주범 검거


T = int(input())
for tc in range(1, T+1):
    row, col, R, C, L = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(row)]
    visited = [[0] * col for _ in range(row)]
    q = [(R, C, L)]
    visited[R][C] = 1

    dr = [[], [-1, 1, 0, 0], [-1, 1], [0, 0], [-1, 0], [1, 0], [1, 0], [-1, 0]]
    dc = [[], [0, 0, -1, 1], [0, 0], [-1, 1], [0, 1], [0, 1], [0, -1], [0, -1]]

    while len(q) > 0:
        cur = q.pop(0)
        cur_r, cur_c, cur_l = cur[0], cur[1], cur[2]

        pipe = MAP[cur_r][cur_c]
        for d in range(len(dr[pipe])):
            nr, nc = cur_r + dr[pipe][d], cur_c + dc[pipe][d]

            if nr < 0 or nc < 0 or row <= nr or col <= nc:
                continue
            if visited[nr][nc] or MAP[nr][nc] == 0:
                continue
            if cur_l - 1 == 0:
                continue

            if pipe == 1:
                if d == 0 and (MAP[nr][nc] == 3 or MAP[nr][nc] == 4 or MAP[nr][nc] == 7):
                    continue
                if d == 1 and (MAP[nr][nc] == 3 or MAP[nr][nc] == 5 or MAP[nr][nc] == 6):
                    continue
                if d == 2 and (MAP[nr][nc] == 2 or MAP[nr][nc] == 6 or MAP[nr][nc] == 7):
                    continue
                if d == 3 and (MAP[nr][nc] == 2 or MAP[nr][nc] == 4 or MAP[nr][nc] == 5):
                    continue

            if pipe == 2:
                if d == 0 and (MAP[nr][nc] == 3 or MAP[nr][nc] == 4 or MAP[nr][nc] == 7):
                    continue
                if d == 1 and (MAP[nr][nc] == 3 or MAP[nr][nc] == 5 or MAP[nr][nc] == 6):
                    continue

            if pipe == 3:
                if d == 0 and (MAP[nr][nc] == 2 or MAP[nr][nc] == 6 or MAP[nr][nc] == 7):
                    continue
                if d == 1 and (MAP[nr][nc] == 2 or MAP[nr][nc] == 4 or MAP[nr][nc] == 5):
                    continue

            if pipe == 4:
                if d == 0 and (MAP[nr][nc] == 3 or MAP[nr][nc] == 4 or MAP[nr][nc] == 7):
                    continue
                if d == 1 and (MAP[nr][nc] == 2 or MAP[nr][nc] == 4 or MAP[nr][nc] == 5):
                    continue

            if pipe == 5:
                if d == 0 and (MAP[nr][nc] == 3 or MAP[nr][nc] == 5 or MAP[nr][nc] == 6):
                    continue
                if d == 1 and (MAP[nr][nc] == 2 or MAP[nr][nc] == 4 or MAP[nr][nc] == 5):
                    continue

            if pipe == 6:
                if d == 0 and (MAP[nr][nc] == 3 or MAP[nr][nc] == 5 or MAP[nr][nc] == 6):
                    continue
                if d == 1 and (MAP[nr][nc] == 2 or MAP[nr][nc] == 6 or MAP[nr][nc] == 7):
                    continue

            if pipe == 7:
                if d == 0 and (MAP[nr][nc] == 3 or MAP[nr][nc] == 4 or MAP[nr][nc] == 7):
                    continue
                if d == 1 and (MAP[nr][nc] == 2 or MAP[nr][nc] == 6 or MAP[nr][nc] == 7):
                    continue

            q.append((nr, nc, cur_l - 1))
            visited[nr][nc] = 1

    ans = 0
    for i in range(row):
        for j in range(col):
            ans += visited[i][j]
    print(f'#{tc} {ans}')
