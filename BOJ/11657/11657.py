# 11657. 타임머신


import sys


def bellman_ford():
    dist = [10000 * N] * (N + 1)  # 걸리는 시간 기록
    dist[1] = 0  # 출발 도시 초기화

    # N회 반복하여 모든 간선을 탐색해 최소 시간 기록
    for repeat in range(1, N + 1):
        for current_node, next_node, cost in edges:
            # 한번도 간 적 없는 노드는 넘어감
            if dist[current_node] == 10000 * N:
                continue

            if dist[current_node] + cost < dist[next_node]:
                dist[next_node] = dist[current_node] + cost

                # N회 반복에 경로가 또 갱신된다면 무한히 도는 음수 사이클 존재
                if repeat == N:
                    return False
    return dist


N, M = map(int, sys.stdin.readline().split())
edges = []  # 간선 저장 배열

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    edges.append([A, B, C])

result = bellman_ford()
if result:
    for city in range(1, N + 1):
        if city == 1:
            continue
        if result[city] == 10000 * N:
            print(-1)
        else:
            print(result[city])
else:
    print(-1)