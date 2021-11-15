# 2667. 단지번호붙이기


import sys
from collections import deque


def bfs(r, c):
    # 한번 함수를 실행하면 붙어있는 모든 집 탐색
    q = deque()
    q.append((r, c))
    cnt = 0  # 집의 수

    while q:
        cr, cc = q.popleft()  # 현재 위치
        cnt += 1
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]  # 다음 위치
            if nr < 0 or N <= nr or nc < 0 or N <= nc:
                continue
            # 집이 아니거나 이미 방문한 경우
            if not MAP[nr][nc] or visited[nr][nc]:
                continue
            visited[nr][nc] = True
            q.append((nr, nc))
    return cnt


N = int(sys.stdin.readline())
MAP = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dr = (-1, 1, 0, 0)  # 상하좌우
dc = (0, 0, -1, 1)

cnt_list = []  # 집의 수 저장 리스트
for row in range(N):
    for col in range(N):
        # 집인데 방문한 적 없는 경우
        if MAP[row][col] and not visited[row][col]:
            visited[row][col] = True
            cnt_list.append(bfs(row, col))
            
cnt_list.sort()  # 오름차순 정렬

print(len(cnt_list))
for cnt_num in cnt_list:
    print(cnt_num)