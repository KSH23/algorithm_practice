# 17836. 공주님을 구해라!


import sys
from collections import deque


row, col, T = map(int, input().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
visited = [[0] * col for _ in range(row)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

visited[0][0] = 1
gram = []
Q = deque()
Q.append((0, 0))

ans = "Fail"

while len(Q) > 0:
    now = Q.popleft()
    now_r = now[0]
    now_c = now[1]

    if visited[now_r][now_c] > T + 1:
        ans = "Fail"
        break

    if now_r == row - 1 and now_c == col -1:
        ans = visited[now_r][now_c] - 1
        break

    for k in range(4):
        nr = now_r + di[k]
        nc = now_c + dj[k]

        if nr < 0 or nc < 0 or row <= nr or col <= nc:
            continue
        if MAP[nr][nc] == 1 or visited[nr][nc] > 0:
            continue

        if MAP[nr][nc] == 2:
            gram = [nr, nc]

        visited[nr][nc] = visited[now_r][now_c] + 1
        Q.append((nr, nc))

if len(gram) > 0:
    using_gram = visited[gram[0]][gram[1]] - 1 + row - 1 - gram[0] + col - 1 - gram[1]
    
    # 그람은 그람으로 이동한 시간이 그래도 T보다 작을 때, 
    # 실패하지 않으면서 기존 경로보다 시간이 짧아진 경우
    # 혹은 실패한 경우 사용 가능하다
    if using_gram > T:
        pass
    elif ans != "Fail" and using_gram < ans:
        ans = using_gram
    elif ans == "Fail":
        ans = using_gram

print(ans)