# 4179. 불!


import sys
from collections import deque


def bfs():
    life = 1  # 지훈이 q에 들어있는 개수
    while q:
        cur = q.popleft()
        row, col = cur[0], cur[1]
        fail = 0  # 지훈이 갈 수 없는 방향의 개수
        if cur[2] == 'J':
            life -= 1
        for d in range(4):
            nr, nc = row + dr[d], col + dc[d]
            if cur[2] == 'F':  # 불의 이동
                if nr < 0 or nc < 0 or R <= nr or C <= nc:
                    continue
                if maze[nr][nc] == '#' or maze[nr][nc] == 'F':
                    continue
                maze[nr][nc] = 'F'
                q.append((nr, nc, 'F'))
            else:  # 지훈의 이동
                if nr < 0 or nc < 0 or R <= nr or C <= nc:
                    return visited[row][col]  # 탈출
                if maze[nr][nc] == '#' or maze[nr][nc] == 'F' or visited[nr][nc]:
                    fail += 1  # 이동 실패
                    continue
                visited[nr][nc] = visited[row][col] + 1  # 방문 표시
                life += 1  # q에 있는 지훈의 개수 증가
                q.append((nr, nc, 'J'))

        if fail == 4 and life == 0:  # 지훈이 q에 없으며 네 방향으로 이동하지 못한 경우
            return 'IMPOSSIBLE'


R, C = map(int, input().split())
J_coord = ()  # 지훈의 위치 좌표
q = deque()
maze = []
for r in range(R):
    temp = list(sys.stdin.readline().rstrip())
    for c in range(C):
        if temp[c] == 'J':
            J_coord = (r, c, 'J')  # 지훈의 좌표 저장
        if temp[c] == 'F':
            q.append((r, c, 'F'))  # 불의 좌표 큐에 추가
    maze.append(temp)
q.append(J_coord)  # 지훈의 좌표를 불 뒤에 추가

visited = [[0] * C for _ in range(R)]  # 지훈의 방문 여부 검사 리스트
visited[J_coord[0]][J_coord[1]] = 1  # 지훈의 시작 좌표 방문 표시

dr = [-1, 1, 0, 0]  # 상하좌우
dc = [0, 0, -1, 1]

print(bfs())