# 2206. 벽 부수고 이동하기


import sys
from collections import deque


def bfs():
    q = deque()
    # 큐에 들어가는 항목: (row, col, 벽을 부신적 있으면 1 / 없으면 0)
    q.append((0, 0, 0))

    while q:
        r, c, did_break = q.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            if nr < 0 or R <= nr or nc < 0 or C <= nc:
                continue  # MAP 바깥
            if visited[nr][nc][did_break]:
                continue  # 이미 방문
            if MAP[nr][nc]:
                if did_break == 0:  # 벽을 만났는데 부술 수 있다면
                    visited[nr][nc][1] = visited[r][c][did_break] + 1
                    q.append((nr, nc, 1))
                continue

            visited[nr][nc][did_break] = visited[r][c][did_break] + 1
            q.append((nr, nc, did_break))


R, C = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(R)]

dr = (-1, 1, 0, 0)  # 상하좌우
dc = (0, 0, -1, 1)

# visited[row][col][0]: 벽을 부시지 않음 / visited[row][col][1]: 벽을 부심
visited = [[[0, 0] for _ in range(C)] for _ in range(R)]
visited[0][0][0] = 1  # 출발 지점
bfs()
ans = min(visited[R - 1][C - 1])
if ans == 0:  # visited[0][0] = [0, X]와 같은 경우
    ans = max(visited[R - 1][C - 1])  # ans를 X로 바꿈
    if ans == 0:  # visited[0][0] = [0, 0]과 같은 경우
        print(-1)
    else:
        print(ans)
else:  # visited[0][0] = [X, Y]와 같은 경우
    print(ans)