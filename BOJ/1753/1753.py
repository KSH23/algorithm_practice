# 1753. 최단경로


import sys


def dijkstra():
    dist = [0] + [11 * V] * V  # 경로의 최소 가중치 저장
    dist[start_node] = 0  # 시작 정점 가중치 초기화
    visited = [0] * (V + 1)

    for _ in range(V):
        min_node, min_w = 0, 11 * V  # 현재 최소 가중치 정보 갱신
        for node in range(1, V + 1):
            if visited[node]:
                continue
            if dist[node] < min_w:
                min_node, min_w = node, dist[node]

        visited[min_node] = 1  # 다음 이동 노드 확정

        for node, weight in graph[min_node]:
            # 현재 노드를 거치는 경우의 가중치가 더 크면 무시
            if dist[node] < weight + min_w:
                continue

            dist[node] = weight + min_w

    return dist


V, E = map(int, input().split())  # 정점의 개수, 간선의 개수
start_node = int(input())  # 시작 정점
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])

result_dist = dijkstra()
for distance in result_dist[1:]:
    if distance == 11 * V:
        print('INF')
    else:
        print(distance)