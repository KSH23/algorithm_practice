# 2468. 안전 영역


import sys
from collections import deque


def bfs(height, cur_r, cur_c):
    q = deque()

    visited[cur_r][cur_c] = 1
    q.append([cur_r, cur_c])

    while q:
        cur = q.popleft()
        row, col = cur[0], cur[1]

        for d in range(4):
            nr, nc = row + dr[d], col + dc[d]
            if nr < 0 or nc < 0 or N <= nr or N <= nc:
                continue
            if MAP[nr][nc] < height or visited[nr][nc] > 0:
                continue

            visited[nr][nc] = 1
            q.appendleft([nr, nc])


N = int(input())

max_height = 0
min_height = 101

MAP = []
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in temp:
        if j < min_height:
            min_height = j    # 최저 높이 갱신
        if max_height < j:
            max_height = j    # 최고 높이 갱신
    MAP.append(temp)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = 0
for h in range(min_height, max_height + 1):
    visited = [[0] * N for _ in range(N)]
    temp = 0    # 안전 영역 개수
    for r in range(N):
        for c in range(N):
            if MAP[r][c] >= h and visited[r][c] == 0:
                # 현재 기준 높이를 방문한 적 없다면 bfs 실행
                bfs(h, r, c)    # [r, c]에 연결된 영역 모두 방문
                temp += 1
    if ans < temp:
        ans = temp

print(ans)