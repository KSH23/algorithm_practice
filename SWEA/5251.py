# 5251. 최소 이동 거리


import heapq


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([w, e])
    dist = [10000001] * 1001  # 시작점부터 [idx]점까지 소요되는 비용

    hq = []  # heapq
    heapq.heappush(hq, [0, 0])
    dist[0] = 0
    while hq:
        now = heapq.heappop(hq)
        now_w, now_point = now[0], now[1]

        for w, next_point in graph[now_point]:
            if dist[next_point] <= dist[now_point] + w:
                continue
            dist[next_point] = dist[now_point] + w
            heapq.heappush(hq, [dist[next_point], next_point])
    print(f'#{tc} {dist[N]}')