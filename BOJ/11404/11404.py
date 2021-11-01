# 11404. 플로이드


import sys
import heapq


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
costs = [[0] * (N + 1) for _ in range(N + 1)]
checked = [[False] * (N + 1) for _ in range(N + 1)]  # 비용이 확정된 경로 표시

hq = []  # heapq

for _ in range(M):
    s_city, e_city, cost = map(int, sys.stdin.readline().split())

    # 만약 이미 비용이 적혀있다면 최솟값으로 갱신
    if costs[s_city][e_city]:
        costs[s_city][e_city] = min(cost, costs[s_city][e_city])
    else:
        costs[s_city][e_city] = cost
    heapq.heappush(hq, (cost, s_city, e_city))  # 비용을 기준으로 힙에 추가

while hq:
    # 비용이 가장 적은 경로 추출
    cost, s_city, e_city = heapq.heappop(hq)

    if checked[s_city][e_city]:  # 이미 확정된 도시는 무시
        continue
    checked[s_city][e_city] = True  # 확정 표시
    costs[s_city][e_city] = cost  # 가격 표시

    for city in range(1, N + 1):  # e_city에서 갈 수 있는 다음 도시
        if city == s_city or city == e_city:
            continue  # 출발지나 도착지(city)와 경유지(e_city)가 같으면 무시

        if costs[e_city][city]:  # city로 갈 수 있는 경로가 있는 경우
            # 새로 만들어진 경로의 비용이 아직 기록되지 않은 경우 힙에 추가
            if costs[s_city][city] == 0:
                heapq.heappush(hq, (cost + costs[e_city][city], s_city, city))
            # 현재 경로의 비용보다 이미 기록된 비용이 저렴할 경우에도 힙에 추가
            elif cost + costs[e_city][city] <= costs[s_city][city]:
                heapq.heappush(hq, (cost + costs[e_city][city], s_city, city))

for row in range(1, N + 1):
    print(' '.join(map(str, costs[row][1:])))