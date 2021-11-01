# 11404. 플로이드


import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
costs = [[0] * (N + 1) for _ in range(N + 1)]


for _ in range(M):
    s_city, e_city, cost = map(int, sys.stdin.readline().split())

    # 만약 이미 비용이 적혀있다면 최솟값으로 갱신
    if costs[s_city][e_city]:
        costs[s_city][e_city] = min(cost, costs[s_city][e_city])
    else:
        costs[s_city][e_city] = cost

for via in range(1, N + 1):  # 경유 도시
    for start in range(1, N + 1):  # 출발 도시
        for end in range(1, N + 1):  # 도착 도시
            if start == end:  # 출발지와 도착지가 같다면 무시
                continue

            # 경유지를 거쳐 갈 수 있는 경우
            if costs[start][via] and costs[via][end]:
                if costs[start][end] == 0:  # 한번도 가보지 않은 경로인 경우
                    costs[start][end] = costs[start][via] + costs[via][end]

                else:  # 이미 가봤던 경로라면 경유 도시의 유무에 따라 최솟값으로 갱신
                    costs[start][end] = min(costs[start][end], \
                                            costs[start][via] + costs[via][end])


for row in range(1, N + 1):
    print(' '.join(map(str, costs[row][1:])))