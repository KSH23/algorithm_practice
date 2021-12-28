# 17143. 낚시왕


import sys


def fish(c):
    weight = 0  # 상어 무게
    for r in range(1, R + 1):
        # 가장 가까운 곳에 있는 상어를 찾음
        if shark_map[r][c]:
            weight = shark_map[r][c]
            shark_map[r][c] = 0  # 상어의 위치를 삭제
            eaten_shark.add(weight)  # 먹힌 상어에 추가
            break
    return weight


def move(r, c, s, d, z):
    # 움직이는 행 또는 열을 결정하고 그에 따른 변수 설정
    if dr[d]:
        n, k, toggle = R, r, 3
        increasing_or_decreasing = dr[d]
    else:
        n, k, toggle = C, c, 7
        increasing_or_decreasing = dc[d]

    # 반복되는 움직임 제거
    move_cnt = (s - 1) % (2 * n - 2) + 1

    if 0 < increasing_or_decreasing:  # 좌표가 증가하는 경우
        # 좌표가 벽을 한 번도 만나지 않은 경우
        if move_cnt <= n - k:
            k += move_cnt
        # 좌표가 벽을 한 번 만나 방향을 바꾼 경우
        elif move_cnt <= (n - k) + (n - 1):
            d = toggle - d  # 방향 전환
            move_cnt -= n - k
            k = n - move_cnt
        # 좌표가 벽을 또 한 번 만나 방향을 또 바꾼 경우
        else:
            k = move_cnt - (2 * n - k - 1) + 1
    else:  # 좌표가 감소하는 경우
        # 좌표가 벽을 한 번도 만나지 않은 경우
        if move_cnt <= k - 1:
            k -= move_cnt
        # 좌표가 벽을 한 번 만나 방향을 바꾼 경우
        elif k - 1 < move_cnt <= (k - 1) + (n - 1):
            d = toggle - d
            move_cnt -= k - 1
            k = 1 + move_cnt
        # 좌표가 벽을 또 한 번 만나 방향을 또 바꾼 경우
        else:
            k = n - (move_cnt - (n + k - 2))

    if toggle == 3:  # 행을 움직인 경우
        nr, nc = k, c 
    else:  # 열을 움직인 경우
        nr, nc = r, k
    
    sharks[z] = (nr, nc, s, d)  # 상어의 정보 갱신
    
    # 현재 좌표에 있는 상어 크기
    shark_in_there = shark_map[nr][nc]
    
    # 현재 좌표에 상어가 있는 경우
    if shark_in_there:
        # 더 큰 상어가 있는 곳으로 간 경우 먹힘
        if z < shark_map[nr][nc]:
            eaten_shark.add(z)
        else:  # 작은 상어가 있다면 먹음
            eaten_shark.add(shark_in_there)
            shark_map[nr][nc] = z
    else:  # 상어가 없는 경우
        shark_map[nr][nc] = z


R, C, M = map(int, sys.stdin.readline().split())

sharks = {}  # 크기를 key로 상어 정보를 저장
shark_map = [[0] * (C + 1) for _ in range(R + 1)]  # 상어 위치에 상어 크기 저장
for _ in range(M):
    row, col, speed, direction, size = map(int, sys.stdin.readline().split())
    sharks[size] = (row, col, speed, direction)
    shark_map[row][col] = size

dr = (0, -1, 1, 0, 0)  # 행 기준 상하우좌
dc = (0, 0, 0, 1, -1)  # 열 기준 상하우좌

current_col = 1  # 현재 사람이 선 열
ans = 0  # 최종 정답
eaten_shark = set()  # 먹힌 상어, 잡힌 상어 저장 세트
while current_col <= C:
    ans += fish(current_col)

    # 상어가 이동한 뒤의 위치를 저장
    shark_map = [[0] * (C + 1) for _ in range(R + 1)]
    for size, shark_info in sharks.items():
        if size in eaten_shark:  # 이미 먹힌 상어는 넘어감
            continue
        row, col, speed, direction = shark_info
        move(row, col, speed, direction, size)
    current_col += 1
print(ans)