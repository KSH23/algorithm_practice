# 2252. 줄 세우기


import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())

edges = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)  # 정점으로의 진입 차수 기록
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    edges[A].append(B)
    in_degree[B] += 1

q = deque()
for node in range(1, N + 1):
    # 진입 차수가 0인 정점을 초깃값으로 추가
    if in_degree[node] == 0:
        q.append(node)

ans = []  # 최종 정답
while q:
    cur_node = q.popleft()  # 현재 노드
    ans.append(cur_node)

    for next_node in edges[cur_node]:
        # 다음 노드의 진입 차수 감소
        in_degree[next_node] -= 1

        # 진입차수가 0이 된 경우 큐에 추가
        if in_degree[next_node] == 0:
            q.append(next_node)

print(' '.join(map(str, ans)))