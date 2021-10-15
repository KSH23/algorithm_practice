# 5250. 최소 비용


import heapq


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    dist = [[10000001] * N for _ in range(N)]
    hq = []
    heapq.heappush(hq, [0, 0])
    dist[0][0] = 0  # 시작 지점에 가는데 드는 비용은 없다

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while hq:  # 다익스트라
        now = heapq.heappop(hq)
        r, c = now[0], now[1]
        h = MAP[r][c]  # 현재 위치의 높이
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or N <= nr or nc < 0 or N <= nc:
                continue

            nh = MAP[nr][nc]  # 다음 칸의 높이
            extra_cost = max(nh - h, 0)  # 다음 칸으로 갈 때 필요한 추가 비용
            if dist[nr][nc] <= extra_cost + dist[r][c] + 1:
                continue
            dist[nr][nc] = extra_cost + dist[r][c] + 1
            heapq.heappush(hq, [nr, nc])

    print(f'#{tc} {dist[N - 1][N - 1]}')