# 16236. 아기 상어


import sys
from collections import deque


def bfs(current_size, sr, sc):
    visited = [[-1] * N for _ in range(N)]
    visited[sr][sc] = 0  # 시작 위치 방문 표시

    q = deque()
    q.append((sr, sc))

    time = -1  # 물고기를 먹을 수 있게 되는 시간
    possible_loc = []  # 물고기를 먹을 수 있는 좌표
    while q:
        cr, cc = q.popleft()
        flag = False  # time이 정해진 후 또 다시 변경되면 True
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if nr < 0 or N <= nr or nc < 0 or N <= nc:
                continue  # 범위 밖
            if -1 < visited[nr][nc]:
                continue  # 이미 방문
            if current_size < MAP[nr][nc] < 9:
                continue  # 더 큰 물고기

            visited[nr][nc] = visited[cr][cc] + 1
            q.append((nr, nc))

            # 이미 더 짧은 시간 안에 물고기를 먹을 수 있는 경우
            if -1 < time < visited[cr][cc] + 1:
                flag = True
                break

            # 물고기를 먹을 수 있는 경우 경우
            if 0 < MAP[nr][nc] < current_size:
                time = visited[cr][cc] + 1
                possible_loc.append((nr, nc))

        # flag가 켜졌거나 가장 마지막 물고기를 먹은 경우
        if flag or (not q and possible_loc):
            # 가장 좌측 상단의 물고기를 선택하도록 정렬
            possible_loc.sort(key=lambda x: (x[0], x[1]))
            # 물고기 제거
            MAP[possible_loc[0][0]][possible_loc[0][1]] = 0
            # 물고기를 먹는데 걸린 시간과 마지막 아기 상어의 위치 반환
            return [visited[cr][cc], possible_loc[0]]


N = int(sys.stdin.readline())
MAP = []
baby_shark_loc = tuple()  # 아기 상어 위치
for r in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    if not baby_shark_loc:  # 아기 상어 위치를 찾지 못한 경우
        for c in range(N):
            if temp[c] == 9:  # 아기 상어 위치 기록
                baby_shark_loc = (r, c)
                temp[c] = 0  # 아기 상어를 나중에 물고기로 착각하지 않도록 제거
    MAP.append(temp)

dr = (-1, 0, 0, 1)  # 상좌우하
dc = (0, -1, 1, 0)

ans = 0  # 최종 정답
baby_shark_size = 2  # 아기 상어 크기
needed_fish_cnt = baby_shark_size  # 성장을 위해 필요한 물고기 수
cnt = 1
while True:
    result = bfs(baby_shark_size, baby_shark_loc[0], baby_shark_loc[1])
    if result:  # 물고기를 먹은 경우
        ans += result[0]  # 시간 갱신
        baby_shark_loc = result[1]  # 아기 상어 위치 갱신
        needed_fish_cnt -= 1
        if needed_fish_cnt == 0:  # 아기 상어 크기 증가
            baby_shark_size += 1
            needed_fish_cnt = baby_shark_size
    else:  # 물고기를 먹지 못한 경우 종료
        print(ans)
        break