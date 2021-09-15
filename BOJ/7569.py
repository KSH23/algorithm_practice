# 7569. 토마토


import sys
from collections import deque


def bfs():
    Q = deque()    # 큐 생성

    di = [-1, 1, 0, 0, 0, 0]  # 상하좌우 + 위아래
    dj = [0, 0, -1, 1, 0, 0]
    dh = [0, 0, 0, 0, 1, -1]

    zero = 0    # (0의 갯수 == 익지 않은 토마토 갯수)를 담는 변수
    for h in range(height):
        for i in range(row):
            for j in range(col):
                if TOMATO[h][i][j] == 1:
                    Q.append([h, i, j])    # 토마토 위치 큐에 추가

                elif TOMATO[h][i][j] == 0:
                    zero += 1    # 안익은 토마토 갯수 추가

    if zero == 0:    # 0이 하나도 없다면 모든 토마토는 이미 익어있는 상태
        return 0

    date = 0    # 토마토가 익는데 걸리는 시간
    while len(Q) > 0:    # BFS 탐색 시작
        now = Q.popleft()
        now_r, now_c, now_h = now[1], now[2], now[0]

        for k in range(6):
            nr, nc, nh = now_r + di[k], now_c + dj[k], now_h + dh[k]

            if nr < 0 or nc < 0 or nh < 0 or row <= nr or col <= nc or height <= nh:
                continue    # TOMATO 상자를 벗어나는 경우 무시
            if TOMATO[nh][nr][nc] == -1 or TOMATO[nh][nr][nc] > 0:
                continue    # 토마토가 없거나 이미 숙성되어 있다면 무시

            date = TOMATO[now_h][now_r][now_c]    # 현재 숙성일자 저장
            zero -= 1    # 토마토가 하나 숙성되었으니 숙성되지 않은 토마토 갯수 감소
            TOMATO[nh][nr][nc] = TOMATO[now_h][now_r][now_c] + 1
            Q.append([nh, nr, nc])

    if zero != 0:    # (0의 갯수 == 익지 않은 토마토 갯수)가 남는 경우
        return -1

    return date


col, row, height = map(int, input().split())
TOMATO = [[list(map(int, sys.stdin.readline().split())) for _ in range(row)] for _ in range(height)]
print(bfs())