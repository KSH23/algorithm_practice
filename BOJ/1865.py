# 1865. 웜홀


import sys


def bellman_ford():
    dist = [10000 * N] * (N + 1)  # 필요 시간 기록
    dist[1] = 0  # 시작 지점 초기화

    for repeat in range(N):
        for start_node, end_node, time in edges:
            # 최소 시간 갱신
            if dist[start_node] + time < dist[end_node]:
                dist[end_node] = dist[start_node] + time
                if repeat == N - 1:  # 음수 사이클이 존재할 경우
                    return 'YES'
    return 'NO'


T = int(sys.stdin.readline())
for _ in range(T):
    N, M, W = map(int, sys.stdin.readline().split())
    edges = []  # 간선 저장 배열
    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        edges.append((S, E, -T))  # 웜홀 저장
    print(bellman_ford())