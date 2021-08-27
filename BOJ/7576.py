# 7576. 토마토


import sys
from collections import deque


col, row = map(int, input().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]

Q = deque()
no_tomato = 0
visited = [[0] * col for _ in range(row)]

for i in range(row):
    for j in range(col):
        if MAP[i][j] == 1:
            Q.append([i, j])
            visited[i][j] = 1
        if MAP[i][j] == -1:
            no_tomato += 1


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


while len(Q) > 0:
    now = Q.popleft()
    now_r = now[0]
    now_c = now[1]

    for k in range(4):
        nr = now_r + di[k]
        nc = now_c + dj[k]
        # print(nr, nc)
        de = 1

        if nr < 0 or nc < 0 or row <= nr or col <= nc:
            continue
        if MAP[nr][nc] == -1 or visited[nr][nc] > 0:
            continue

        MAP[nr][nc] = 1
        visited[nr][nc] = visited[now_r][now_c] + 1
        Q.append([nr, nc])


# for i in range(row):
#     print(visited[i])


max_cnt = 0
no_0 = 0
for i in range(row):
    for j in range(col):
        if visited[i][j] > max_cnt:
            max_cnt = visited[i][j]
        if visited[i][j] == 0:
            no_0 += 1


ans = 0
if no_0 != no_tomato:
    ans = -1
else:
    ans = max_cnt - 1

print(ans)