# 5188. 최소합


def dfs(coord, cost):
    for d in range(2):
        nr, nc = coord[0] + dr[d], coord[1] + dc[d]
        if N <= nr or N <= nc:  # 맵을 벗어나는 경우
            continue
        new_cost = cost + MAP[nr][nc]  # 다음 칸의 비용
        if 0 < dp[nr][nc] < new_cost:
            continue
        dp[nr][nc] = new_cost  
        dfs((nr, nc), new_cost)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]  # (r, c)까지의 최소 비용 저장
    dp[0][0] = MAP[0][0]

    dr = [1, 0]  # 하, 우
    dc = [0, 1]

    ans = N * N * 10  # 최종 정답
    dfs((0, 0), MAP[0][0])
    print(f'#{tc} {dp[N - 1][N - 1]}')