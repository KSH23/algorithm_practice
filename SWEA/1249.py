# 1249. 보급로


import heapq


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]

    hq = []  # heapq
    dist = [[987654321] * N for _ in range(N)]

    # 초기 지점
    dist[0][0] = 0
    heapq.heappush(hq, [0, 0])

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while hq:  # 다익스트라
        r, c = heapq.heappop(hq)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or N <= nr or nc < 0 or N <= nc:
                continue
            if dist[nr][nc] <= dist[r][c] + MAP[nr][nc]:
                continue
            dist[nr][nc] = dist[r][c] + MAP[nr][nc]
            heapq.heappush(hq, [nr, nc])

    print(f'#{tc} {dist[N - 1][N - 1]}')