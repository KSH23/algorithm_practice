# 1012. 유기농 배추


import sys
from collections import deque


def bfs(r, c):
    q = deque()
    q.append((r, c))  # 출발 지점 표시

    dr = [-1, 1, 0, 0]  # 상하좌우
    dc = [0, 0, -1, 1]

    while q:
        cur_r, cur_c = q.popleft()
        for d in range(4):
            nr, nc = cur_r + dr[d], cur_c + dc[d]
            if nr < 0 or R <= nr or nc < 0 or C <= nc:
                continue  # 농장을 벗어나는 경우
            if visited[nr][nc] or farm[nr][nc] == 0:
                continue  # 이미 방문했거나 배추가 없는 경우
            visited[nr][nc] = 1  # 방문 표시
            q.append((nr, nc))


T = int(input())
for _ in range(T):
    C, R, K = map(int, sys.stdin.readline().split())
    farm = [[0] * C for _ in range(R)]
    for _ in range(K):
        col, row = map(int, sys.stdin.readline().split())
        farm[row][col] = 1

    visited = [[0] * C for _ in range(R)]  # 방문 표시
    cnt = 0  # 필요한 수
    for row in range(R):
        for col in range(C):
            # 배추가 있고 방문한 적 없는 경우
            if farm[row][col] and visited[row][col] == 0:
                bfs(row, col)
                cnt += 1
    print(cnt)