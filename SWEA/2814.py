# 2814. 최장 경로


def dfs(now, cnt):
    global ans

    ans = max(ans, cnt)  # 경로 갱신

    for node in range(1, N + 1):
        if visited[node]:
            continue
        if MAP[now][node]:
            visited[node] = 1
            dfs(node, cnt + 1)
            visited[node] = 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    MAP = [[0] * (N + 1) for _ in range(N + 1)]  # 연결관계 표시
    for _ in range(M):
        x, y = map(int, input().split())
        MAP[x][y] = 1
        MAP[y][x] = 1
    visited = [0] * (N + 1)
    ans = 0  # 최종 정답
    for start in range(1, N + 1):
        visited[start] = 1
        dfs(start, 1)
        visited[start] = 0

    print(f'#{tc} {ans}')