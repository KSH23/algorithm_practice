# 3124. 최소 스패닝 트리(Prim's algorithm)


import heapq


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V + 1)]  # 연결 리스트
    for _ in range(E):
        A, B, weight = map(int, input().split())
        adj_list[A].append([weight, B])
        adj_list[B].append([weight, A])

    hq = []  # heapq
    visited = [0] * (V + 1)
    for w, node in adj_list[1]:  # heapq 초기값 설정
        heapq.heappush(hq, (w, node))  # w를 기준으로 설정
    visited[1] = 1  # 초기값 설정

    total_weight = 0
    while hq:
        now = heapq.heappop(hq)
        w, node = now[0], now[1]
        if visited[node]:
            continue
        total_weight += w
        visited[node] = 1
        for w, node in adj_list[node]:
            heapq.heappush(hq, (w, node))

    print(f'#{tc} {total_weight}')