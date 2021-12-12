# 1504. 특정한 최단 경로


import sys
import heapq


def dijkstra(start_node, last_node):
    hq = []  # heapq
    heapq.heappush(hq, [0, start_node])  # 시작 정점 추가
    dist = [0] + [1001 * N] * N  # 경로의 최소 가중치 저장
    dist[start_node] = 0  # 시작 정점 가중치 초기화
    visited = [0] * (N + 1)

    while hq:
        now_distance, now_node = heapq.heappop(hq)
        if visited[now_node]:  # 이미 확정된 노드는 무시
            continue
        visited[now_node] = 1

        for distance, next_node in edges[now_node]:
            # 현재 노드를 거치는 경우의 가중치가 더 크면 무시
            if dist[next_node] <= distance + now_distance:
                continue
            dist[next_node] = distance + now_distance
            heapq.heappush(hq, [dist[next_node], next_node])

    if dist[last_node] == 1001 * N:
        return -1001 * N
    return dist[last_node]


N, E = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(N + 1)]  # 간선 저장 배열
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[a].append([c, b])  # 거리 기준으로 저장
    edges[b].append([c, a])

node1, node2 = map(int, sys.stdin.readline().split())  # 경유 필수 정점
default_dist = dijkstra(node1, node2)  # 경유 필수 정점간 거리
dist_from_1_to_node1 = dijkstra(1, node1)
dist_from_1_to_node2 = dijkstra(1, node2)
dist_from_node1_to_N = dijkstra(node1, N)
dist_from_node2_to_N = dijkstra(node2, N)

route1 = max(-1, dist_from_1_to_node1 + dist_from_node2_to_N)
route2 = max(-1, dist_from_1_to_node2 + dist_from_node1_to_N)

if default_dist == -1001 * N:  # 경유 필수 정점이 이어지지 않은 경우
    print(-1)
elif route1 == 0 and route2 == 0:  # route1과 route2가 불가능한 경로인 경우
    print(-1)

elif route1 == -1:  # route1이 불가능한 경로인 경우
    if 1 == node2 and N == node1:  # 경유 노드와 시작, 도착 노드가 같은 경우
        print(route2)
    else:
        print(route2 + default_dist)
elif route2 == -1:  # route2가 불가능한 경로인 경우
    if 1 == node1 and N == node2:  # 경유 노드와 시작, 도착 노드가 같은 경우
        print(route1)
    else:
        print(route1 + default_dist)
else:  # route1과 route2 둘 다 가능한 경로인 경우
    if 1 == node2 and N == node1:
        if 1 == node1 and N == node2:
            print(0)
        else:
            print(default_dist)
    else:
        if 1 == node1 and N == node2:
            print(default_dist)
        else:
            print(default_dist + min(route1, route2))