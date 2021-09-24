# 2636. 치즈


import sys
from collections import deque


def bfs():
    global last_cheese

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    q = deque()
    q.append([0, 0, False])
    visited[0][0] = 0

    while q:
        cur = q.popleft()
        cur_r, cur_c, cur_cheese = cur[0], cur[1], cur[2]
        last_cheese = visited[cur_r][cur_c]
        
        for d in range(4):
            nr, nc = cur_r + dr[d], cur_c + dc[d]
            if nr < 0 or nc < 0 or row <= nr or col <= nc or visited[nr][nc] > -1:
                continue

            if MAP[nr][nc]:  # 다음 칸이 치즈일 경우
                visited[nr][nc] = visited[cur_r][cur_c] + 1
                q.append([nr, nc, True])
            else:    # 다음 칸이 공기일 경우
                visited[nr][nc] = visited[cur_r][cur_c]
                q.appendleft([nr, nc, False])


row, col = map(int, input().split())
MAP = [list(map(int, sys.stdin.readline().split()))for _ in range(row)]
visited = [[-1] * col for _ in range(row)]
last_cheese = 0    # 치즈가 모두 녹아서 없어지는 데 걸리는 시간
bfs()

cheese_cnt = 0    # 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수
for i in range(row):
    for j in range(col):
        # 마지막 치즈의 visited 값과 그 안 공기의 visited 값은 같기 때문에
        # 치즈만 골라서 따로 개수를 센다
        if visited[i][j] == last_cheese and MAP[i][j]:
            cheese_cnt += 1

print(last_cheese)
print(cheese_cnt)