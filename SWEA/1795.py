# 1795. 인수의 생일 파티


import heapq


def dijkstra(cost_map):
    hq = []  # heapq
    dist = [100000] * (N + 1)

    # 시작 지점을 X로 초기화
    heapq.heappush(hq, [0, X])
    dist[X] = 0

    while hq:  # 다익스트라
        now = heapq.heappop(hq)
        now_cost, now_house = now[0], now[1]
        for next_house in range(1, N + 1):  # 다음에 갈 수 있는 집 갱신
            if dist[next_house] <= dist[now_house] + cost_map[now_house][next_house]:
                continue
            dist[next_house] = dist[now_house] + cost_map[now_house][next_house]

            heapq.heappush(hq, [dist[next_house], next_house])

    return dist


T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    MAP = [[100000] * (N + 1) for _ in range(N + 1)]  # 문제에서 제시된 지도
    REVERSE_MAP = [[100000] * (N + 1) for _ in range(N + 1)]  # 방향을 바꾼 지도
    for _ in range(M):
        x, y, c = map(int, input().split())
        MAP[x][y] = c
        REVERSE_MAP[y][x] = c

    X_to_house_dist = dijkstra(MAP)

    # 방향을 바꾼 지도를 사용하여 임의의 집에서 X까지 가는 경우를 계산
    house_to_X_dist = dijkstra(REVERSE_MAP)

    max_cost = 0
    for h in range(1, N + 1):
        if h == X:
            continue
        max_cost = max(max_cost, X_to_house_dist[h] + house_to_X_dist[h])

    print(f'#{tc} {max_cost}')