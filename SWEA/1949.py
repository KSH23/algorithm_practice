# 1949. 등산로 조성


def dfs(r, c, cnt, do_dig):
    global longest

    if cnt > longest:
        longest = cnt
        # for ii in range(N):
        #     print(visited[ii])
        # print('---------------------------')

    dr = [-1, 1, 0, 0]  # 상하좌우
    dc = [0, 0, -1, 1]

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if nr < 0 or nc < 0 or N <= nr or N <= nc or visited[nr][nc]:
            continue
        if do_dig == 1 and MAP[nr][nc] >= MAP[r][c]:
            continue
        if MAP[nr][nc] - K >= MAP[r][c]:
            continue
        elif MAP[nr][nc] >= MAP[r][c] and do_dig == 0:
            for dig in range(1, K + 1):
                if MAP[nr][nc] - dig < MAP[r][c]:
                    temp = MAP[nr][nc]
                    MAP[nr][nc] -= dig
                    visited[nr][nc] = 1
                    dfs(nr, nc, cnt + 1, 1)
                    visited[nr][nc] = 0
                    MAP[nr][nc] = temp
            continue

        visited[nr][nc] = 1
        dfs(nr, nc, cnt + 1, do_dig)
        visited[nr][nc] = 0


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    highest_list = []
    highest_value = 0

    for i in range(N):
        for j in range(N):
            if MAP[i][j] > highest_value:
                highest_list = [(i, j)]
                highest_value = MAP[i][j]
            elif MAP[i][j] == highest_value:
                highest_list.append((i, j))

    longest = 0
    visited = [[0] * N for _ in range(N)]

    for peak in highest_list:
        visited[peak[0]][peak[1]] = 1
        dfs(peak[0], peak[1], 1, 0)
        visited[peak[0]][peak[1]] = 0

    print(f'#{tc} {longest}')
