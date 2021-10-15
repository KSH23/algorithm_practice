# 1251. 하나로


import heapq


def calc_dist(x1, x2, y1, y2):
    dx = x1 - x2
    dy = y1 - y2
    return dx ** 2 + dy ** 2  # 두 좌표 사이 거리 반환


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x = list(map(int, input().split()))  # x 좌표
    y = list(map(int, input().split()))  # y 좌표
    E = float(input())
    MAP = [[0] * N for _ in range(N)]  # 비용 저장 리스트
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            MAP[i][j] = calc_dist(x[i], x[j], y[i], y[j])
            MAP[j][i] = MAP[i][j]

    hq = []  # heapq
    visited = [0] * N

    # 시작 섬을 0번 섬으로 초기화
    for island in range(1, N):
        heapq.heappush(hq, [MAP[0][island], island])
    visited[0] = 1

    total_cost = 0  # 최종 비용
    while hq:  # MST
        now = heapq.heappop(hq)
        now_cost, next_island = now[0], now[1]
        if visited[next_island]:  # 방문한 적 있으면 무시
            continue
        total_cost += now_cost
        visited[next_island] = 1  # 방문 표시
        for island in range(1, N):  # 다음에 갈 수 있는 섬 갱신
            if visited[island]:
                continue
            heapq.heappush(hq, [MAP[next_island][island], island])

    print(f'#{tc} {round(total_cost * E)}')