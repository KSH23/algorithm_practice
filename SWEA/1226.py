# 1226. 미로1


for tc in range(1, 11):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]

    now_r = now_c = 0
    flag = 0
    for i in range(16):
        if flag == 1:
            break
        for j in range(16):
            if MAP[i][j] == 2:
                now_r = i
                now_c = j
                visited[now_r][now_c] = 1
                flag = 1
                break

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    Q = [(now_r, now_c)]
    visited[now_r][now_c] = 1
    ans = 0

    while ans == 0 and len(Q) > 0:
        now = Q.pop(0)
        now_r = now[0]
        now_c = now[1]

        for k in range(4):
            nr = now_r + di[k]
            nc = now_c + dj[k]
            if nr < 0 or nc < 0 or 16 <= nr or 16 <= nc:
                continue
            if MAP[nr][nc] == 1 or visited[nr][nc] > 0:
                continue

            visited[nr][nc] = 1

            if MAP[nr][nc] == 3:
                ans = 1
                break

            Q.append((nr, nc))
    de=1
    print('#{} {}'.format(tc, ans))