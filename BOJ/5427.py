# 5427. 불


import sys
from collections import deque


def bfs():
    while q:
        cur = q.popleft()
        row, col = cur[0], cur[1]
        for d in range(4):
            nr, nc = row + dr[d], col + dc[d]
            if cur[2] == '*':  # 불의 이동
                if nr < 0 or nc < 0 or R <= nr or C <= nc:
                    continue
                if maze[nr][nc] == '#' or maze[nr][nc] == '*':
                    continue
                maze[nr][nc] = '*'
                q.append((nr, nc, '*'))
            else:  # 상근의 이동
                cnt = cur[3]  # 상근의 이동 시간
                if nr < 0 or nc < 0 or R <= nr or C <= nc:
                    return cnt  # 탈출
                if not maze[nr][nc] == '.':
                    continue
                maze[nr][nc] = '@'
                q.append((nr, nc, '@', cnt + 1))

    return -1  # 탈출 실패


T = int(input())
for test in range(T):
    C, R = map(int, sys.stdin.readline().split())
    location = ()  # 상근의 위치 좌표
    q = deque()
    maze = []
    for r in range(R):
        temp = list(sys.stdin.readline().rstrip())
        for c in range(C):
            if temp[c] == '@':
                location = (r, c, '@', 1)  # 상근의 좌표 저장
            elif temp[c] == '*':
                q.append((r, c, '*'))  # 불의 좌표 큐에 추가
        maze.append(temp)
    q.append(location)  # 상근의 좌표를 불 뒤에 추가

    dr = [-1, 1, 0, 0]  # 상하좌우
    dc = [0, 0, -1, 1]

    ans = bfs()
    if ans == -1:
        print('IMPOSSIBLE')
    else:
        print(ans)