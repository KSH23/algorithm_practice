# 14938. 서강그라운드


import sys


N, M, R = map(int, sys.stdin.readline().split())
T = [0] + list(map(int, sys.stdin.readline().split()))
dist = [[16 * N] * (N + 1) for _ in range(N + 1)]  # 거리 기록
for _ in range(R):
    node1, node2, length = map(int, sys.stdin.readline().split())
    dist[node1][node2] = dist[node2][node1] = length

# 플로이드-와샬 알고리즘을 이용해 모든 정점에서 모든 정점으로 가는 거리 탐색
for via in range(1, N + 1):  # 경유 정점
    for start in range(1, N + 1):  # 시작 정점
        for end in range(1, N + 1):  # 도착 정점
            if start == end:
                continue
            # 갈 수 있는 경유 최단거리 갱신
            if dist[start][via] and dist[via][end]:
                if dist[start][via] + dist[via][end] < dist[start][end]:
                    dist[start][end] = dist[start][via] + dist[via][end]
ans = 0
for node in range(1, N + 1):
    temp = T[node]
    for next_node in range(1, N + 1):
        if node == next_node:
            continue
        # 수색 범위 밖의 정점은 무시
        if M < dist[node][next_node]:
            continue
        temp += T[next_node]
    ans = max(ans, temp)

print(ans)