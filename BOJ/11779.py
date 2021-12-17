# 11779. 최소비용 구하기 2


import sys
import heapq


def dijkstra():
    hq = []
    costs = [100001 * N] * (N + 1)

    # 힙에 비용을 기준으로 경로와 함께 저장
    heapq.heappush(hq, [0, START, [START]])
    costs[START] = 0  # 시작 지점 초기화

    while hq:
        cur_cost, cur_node, cur_path = heapq.heappop(hq)

        if cur_node == END:  # 목표 지점 도착
            print(cur_cost)
            print(len(cur_path))
            print(' '.join(map(str, cur_path)))
            return

        for next_cost, next_node in edges[cur_node]:
            # 최소 비용으로 갈 수 있는 경우 이를 갱신하고 힙에 다음 노드 추가
            if next_cost + costs[cur_node] < costs[next_node]:
                costs[next_node] = next_cost + costs[cur_node]
                heapq.heappush(hq, [costs[next_node], next_node, cur_path + [next_node]])


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
edges = [[] for _ in range(N + 1)]  # 간선 저장 배열
for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    edges[start].append([cost, end])

START, END = map(int, sys.stdin.readline().split())
dijkstra()