# 1753. 최단경로(heapq 사용)


import sys
import heapq


def dijkstra():
    hq = []  # heapq
    heapq.heappush(hq, [0, start_node])  # 시작 정점 추가
    dist = [0] + [11 * V] * V  # 경로의 최소 가중치 저장
    dist[start_node] = 0  # 시작 정점 가중치 초기화
    visited = [0] * (V + 1)

    while hq:
        now_w, now_node = heapq.heappop(hq)
        if visited[now_node]:  # 이미 확정된 노드는 무시
            continue
        visited[now_node] = 1

        for weight, next_node in graph[now_node]:
            # 현재 노드를 거치는 경우의 가중치가 더 크면 무시
            if dist[next_node] <= weight + now_w:
                continue
            dist[next_node] = weight + now_w  # 가중치 갱신
            heapq.heappush(hq, [dist[next_node], next_node])

    return dist


V, E = map(int, input().split())  # 정점의 개수, 간선의 개수
start_node = int(input())  # 시작 정점
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([w, v])  # 가중치를 기준으로 저장

result_dist = dijkstra()
for distance in result_dist[1:]:
    if distance == 11 * V:
        print('INF')
    else:
        print(distance)