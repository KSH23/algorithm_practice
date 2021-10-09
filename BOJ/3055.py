# 3055. 탈출


import sys
from collections import deque


def bfs():
    while q:
        cur = q.popleft()
        is_hedgehog, row, col = cur[0], cur[1], cur[2]

        for d in range(4):
            nr, nc = row + dr[d], col + dc[d]

            if nr < 0 or nc < 0 or R <= nr or C <= nc:
                continue
            if MAP[nr][nc] == 'X':
                continue
            if is_hedgehog:    # 고슴도치의 좌표가 들어온 경우
                if visited[nr][nc] > -1 or MAP[nr][nc] == '*':
                    continue
                q.append([1, nr, nc])
                visited[nr][nc] = visited[row][col] + 1
                if nr == beaver[0] and nc == beaver[1]:
                    return visited[nr][nc]
            else:    # 물의 좌표가 들어온 경우
                if MAP[nr][nc] == '.' or MAP[nr][nc] == 'S':
                    MAP[nr][nc] = '*'
                    q.append([0, nr, nc])
    return 0


R, C = map(int, input().split())
beaver = []    # 비버의 굴 위치
q = deque()    # 큐 생성
visited = [[-1] * C for _ in range(R)]
MAP = []    # 숲의 지도
for i in range(R):
    temp = list(sys.stdin.readline().rstrip())
    for j in range(C):
        if temp[j] == 'D':
            beaver = [i, j]    # 비버의 굴 위치 저장
        elif temp[j] == '*':
            q.appendleft([0, i, j])    # 물을 먼저 bfs 진행
        elif temp[j] == 'S':
            q.append([1, i, j])
            visited[i][j] = 0    # 고슴도치 위치를 큐에 저장
    MAP.append(temp)

dr = [-1, 1, 0, 0]    # 상하좌우
dc = [0, 0, -1, 1]

ans = bfs()
if ans:
    print(ans)
else:    # 비버의 굴에 도착하지 못한 경우
    print('KAKTUS')