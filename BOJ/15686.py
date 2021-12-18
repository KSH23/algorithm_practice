# 15686. 치킨 배달


import sys


def select_chicken(cur_row, row_cnt, cur_dist, selected_dist):
    global ans

    if row_cnt == M:  # M개의 치킨집을 고른 경우
        ans = min(ans, cur_dist)
        return

    if len(chickens) <= cur_row:  # 범위 밖
        return

    cur_selected_dist = selected_dist[:]  # 현재 계산된 최소 치킨 거리 복사

    # 현재 치킨집을 고르지 않는 경우
    select_chicken(cur_row + 1, row_cnt, cur_dist, cur_selected_dist)

    # 현재 치킨집을 고르는 경우 새로 생기는 치킨 거리를 통해 최소 거리를 탐색
    for i in range(len(houses)):
        # 계산된 치킨 거리를 최솟값으로 갱신
        if dist[cur_row][i] < cur_selected_dist[i]:
            cur_selected_dist[i] = dist[cur_row][i]
    select_chicken(cur_row + 1, row_cnt + 1, sum(cur_selected_dist), cur_selected_dist)


N, M = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

chickens = []  # 치킨집 위치 저장
houses = []  # 집 위치 저장
for row in range(N):
    for col in range(N):
        if MAP[row][col] == 1:
            houses.append([row, col])
        elif MAP[row][col] == 2:
            chickens.append([row, col])

# 행은 치킨집의 인덱스, 열은 집의 인덱스를 갖고 거리를 저장하는 2차원 배열
dist = [[0] * len(houses) for _ in range(len(chickens))]
for col_idx, house in enumerate(houses):
    for row_idx, chicken in enumerate(chickens):
        distance = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
        dist[row_idx][col_idx] = distance

ans = 2500  # 최종 정답
select_chicken(0, 0, 0, [2500] * len(houses))
print(ans)