# 16946. 벽 부수고 이동하기 4


import sys
from collections import deque


def bfs(r, c):
    dr = [-1, 1, 0, 0]  # 상하좌우
    dc = [0, 0, -1, 1]  # 상하좌우

    q = deque()
    q.append([r, c])  # 시작 지점 추가

    walls = set()  # 주위 벽의 좌표 저장

    cnt = 1  # 이동할 수 있는 칸의 개수
    while q:
        now_r, now_c = q.popleft()
        for d in range(4):
            nr, nc = now_r + dr[d], now_c + dc[d]
            if nr < 0 or R <= nr or nc < 0 or C <= nc:
                continue
            if visited[nr][nc]:
                continue

            # 벽을 만난 경우 벽의 좌표를 저장
            if matrix[nr][nc]:
                walls.add((nr, nc))
                continue

            visited[nr][nc] = 1
            cnt += 1
            q.append([nr, nc])

    # 만난 모든 벽에 대하여 이동 가능한 칸의 개수를 추가
    for wall_r, wall_c in list(walls):
        matrix[wall_r][wall_c] += cnt


R, C = map(int, input().split())
matrix = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]  # 이동한 지점을 표시
for row in range(R):
    for col in range(C):
        if matrix[row][col] == 0 and visited[row][col] == 0:
            visited[row][col] = 1  # 출발 지점 표시
            bfs(row, col)

for row in range(R):
    for col in range(C):
        print(matrix[row][col] % 10, end='')
    print()