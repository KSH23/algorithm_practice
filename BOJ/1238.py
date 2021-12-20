# 1238. 파티


import sys
import heapq


def dijkstra(start_node, end_node):
    hq = []
    heapq.heappush(hq, [0, start_node])
    dist = [-1] * (N + 1)
    dist[start_node] = 0
    while hq:
        cur_cost, cur_node = heapq.heappop(hq)
        if start_node != end_node and cur_node == end_node:
            return cur_cost
        for next_node, cost in edges[cur_node]:
            if dist[next_node] == -1 or cur_cost + cost < dist[next_node]:
                dist[next_node] = cur_cost + cost
                heapq.heappush(hq, [dist[next_node], next_node])

    return dist


N, M, X = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(N + 1)]  # 간선 저장 배열
for _ in range(M):
    s, e, t = map(int, sys.stdin.readline().split())
    edges[s].append([e, t])

time = [0] * (N + 1)  # 각 node에서 소요되는 시간 기록
for node in range(1, N + 1):
    result = dijkstra(node, X)
    if node == X:
        # 파티가 열리는 노드에서 출발하는 경우 모든 노드에 대한 결과를 받음
        # 이를 모든 노드에 대하여 각각 그 결과를 추가
        for n in range(1, N + 1):
            time[n] += result[n]
    else:
        # 파티가 열리는 노드까지 가는데 걸리는 시간 추가
        time[node] += result
print(max(time))
