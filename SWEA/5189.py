# 5189. 전자카트


def dfs(now, park_cnt, cost):
    global ans

    if park_cnt == N:
        ans = min(ans, cost + BATTERY[now][0])
        return

    for park in range(1, N):
        if visited[park]:
            continue
        visited[park] = 1
        dfs(park, park_cnt + 1, cost + BATTERY[now][park])
        visited[park] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    BATTERY = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N  # 방문 표시
    visited[0] = 1
    ans = N * N * 100  # 최종 정답
    dfs(0, 1, 0)
    print(f'#{tc} {ans}')