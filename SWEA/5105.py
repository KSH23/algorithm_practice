# 5105. 미로의 거리


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    now_r = now_c = 0
    flag = 0
    for i in range(N):
        if flag == 1:
            break
        for j in range(N):
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
    ans = ()

    while len(Q) > 0:
        now = Q.pop(0)
        now_r = now[0]
        now_c = now[1]

        if len(ans) > 0:
            break

        for k in range(4):
            nr = now_r + di[k]
            nc = now_c + dj[k]
            if nr < 0 or nc < 0 or N <= nr or N <= nc:
                continue
            if MAP[nr][nc] == 1 or visited[nr][nc] > 0:
                continue

            visited[nr][nc] = visited[now_r][now_c] + 1

            if MAP[nr][nc] == 3:
                ans = (nr, nc)
                break

            Q.append((nr, nc))

    if len(ans) == 0:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, visited[ans[0]][ans[1]] - 2))