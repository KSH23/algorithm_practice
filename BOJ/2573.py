# 2573. 빙산


import sys
from collections import deque


def do_melt(start_r, start_c):
    q = deque()
    q.append([start_r, start_c])
    visited[start_r][start_c] = check_num
    melt_list = []
    while q:
        cur = q.popleft()
        row, col = cur[0], cur[1]
        temp = 0  # 주변 바다의 갯수
        for d in range(4):
            nr, nc = row + dr[d], col + dc[d]
            if nr < 0 or nc < 0 or N <= nr or M <= nc:
                continue
            if visited[nr][nc] >= check_num:
                continue
            if iceberg[nr][nc] == 0:
                temp += 1  # 주변 바다의 갯수 갱신
                continue

            q.append([nr, nc])
            visited[nr][nc] = check_num
        melt_list.append([row, col, temp])

    melted_iceberg_cnt = 0  # 녹은 빙산의 총 갯수
    for item in melt_list:
        # 주변 바다의 갯수만큼 빙산을 녹이고 갯수 갱신
        iceberg[item[0]][item[1]] -= item[2]
        if iceberg[item[0]][item[1]] <= 0:
            iceberg[item[0]][item[1]] = 0
            melted_iceberg_cnt += 1

    return melted_iceberg_cnt


def bfs(start_r, start_c):
    q = deque()
    q.append([start_r, start_c])
    visited[start_r][start_c] = check_num
    iceberg_cnt = 1  # 빙산의 수
    while q:
        cur = q.popleft()
        row, col = cur[0], cur[1]

        for d in range(4):
            nr, nc = row + dr[d], col + dc[d]
            if nr < 0 or nc < 0 or N <= nr or M <= nc:
                continue
            if iceberg[nr][nc] == 0:
                continue
            if visited[nr][nc] == check_num:
                continue

            q.append([nr, nc])
            visited[nr][nc] = check_num
            iceberg_cnt += 1

    return iceberg_cnt


N, M = map(int, sys.stdin.readline().split())
initial_iceberg_cnt = 0  # 존재하는 빙산의 갯수
iceberg = []
for i in range(N):
    temp_iceberg = list(map(int, sys.stdin.readline().split()))
    for j in range(1, M - 1):
        if temp_iceberg[j]:
            initial_iceberg_cnt += 1
    iceberg += [temp_iceberg]

visited = [[0] * M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# visited 리스트에 기록될 값, 이 값을 통해 빙산이 녹은 시점을 기록
check_num = 1
year = 0    # 걸리는 시간

while True:
    remain_iceberg = melted_iceberg = 0
    melt = 0  # 빙산이 녹는 과정이 실행되었는지 표시
    switch = 0  # 이중 for loop 탈출 위한 값
    for i in range(1, N - 1):
        if switch:
            break
        for j in range(1, M - 1):
            # 빙산이 존재하고 아직 녹는 과정이 진행되지 않은 경우
            if iceberg[i][j] > 0 and melt == 0:
                melted_iceberg = do_melt(i, j)  # 녹은 빙산의 수
                year += 1
                melt = 1  # 녹는 과정 실행 표시
                check_num += 1

            # 녹는 과정이 진행되었고 빙산을 만나면
            # bfs를 통해 현재 연결되어있는 빙산의 수만 확인
            if iceberg[i][j] > 0 and melt:
                remain_iceberg = bfs(i, j)
                switch = 1
                break

    if remain_iceberg == 0:  # 남은 빙산이 없는 경우
        year = 0
        break

    # 초기 빙산의 수와 녹은 빙산, 남은 빙산의 수의 합이 다르다면 분리가 된 것
    if initial_iceberg_cnt != melted_iceberg + remain_iceberg:
        break
    
    # 초기 빙산의 수 갱신
    initial_iceberg_cnt = remain_iceberg
    check_num += 1

print(year)