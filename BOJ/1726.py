# 1726. 로봇


import sys
from collections import deque


row, col = map(int, input().split())

# 주어진 좌표를 그대로 이용하기 위하여 상단과 좌측에 벽을 한 곂 생성
MAP = [[1] * (col + 1)] + [[1] + list(map(int, sys.stdin.readline().split())) for _ in range(row)]
start = list(map(int, input().split()))    # 출발 지점
end = list(map(int, input().split()))    # 도착 지점

# 방향이 X일 때 X를 인덱스로 호출할 수 있도록 하며, 호출시 좌측과 우측의 방향을 전달
turn_list = [[], [4, 3], [3, 4], [1, 2], [2, 1]]

# 방문했던 지점을 방향과 함께 기록, 방향 값을 그대로 인덱스 호출할 수 있도록 함
visited = [[[0, 0, 0, 0, 0] for _ in range(col + 1)] for _ in range(row + 1)]
visited[start[0]][start[1]][start[2]] = 1    # 시작 지점 초기화

dr = [0, 0, 0, 1, -1]    # 0 + 동서남북
dc = [0, 1, -1, 0, 0]

q = deque()    # 큐 생성
q.append(start)

while q:    # BFS 실행
    cur = q.popleft()
    r, c, direction = cur[0], cur[1], cur[2]

    for k in range(1, 4):    # Go 명령 수행
        nr, nc = r + dr[direction] * k, c + dc[direction] * k

        if nc < 1 or nc < 1 or row < nr or col < nc:
            break    # 맵 밖으로 벗어나면 무시
        if MAP[nr][nc]:
            break    # 벽을 만나면 무시
        if visited[nr][nc][direction]:
            continue  # 계속 놓친 부분, 이미 방문한 지점이라면 break가 아닌 continue
        q.append([nr, nc, direction])
        visited[nr][nc][direction] = visited[r][c][direction] + 1

    for d in turn_list[direction]:    # Turn dir 명령 수행
        if visited[r][c][d]:    # 이미 방문한 지점이라면 무시
            continue
        q.append([r, c, d])
        visited[r][c][d] = visited[r][c][direction] + 1

print(visited[end[0]][end[1]][end[2]] - 1)