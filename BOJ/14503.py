# 14503. 로봇 청소기


N, M = map(int, input().split())
row, col, direction = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

cur = [row, col, direction]    # 현재 위치
ans = 0    # 청소한 칸의 개수

dr = [-1, 0, 1, 0]    # row 북동남서
dc = [0, 1, 0, -1]    # col 북동남서

while True:
    cur_r, cur_c, cur_d = cur[0], cur[1], cur[2]

    if MAP[cur_r][cur_c] == 0:    # 1. 현재 위치를 청소한다
        MAP[cur_r][cur_c] = 2    # 벽과 구분되도록 2로 표시
        ans += 1

    flag = 0    # 이 변수가 4가 되면 네 방향 모두 가지 못한 것
    for _ in range(4):
        # 2. 현재 방향을 기준으로 왼쪽 방향을 탐색한다
        nd = (cur_d + 3) % 4
        nr, nc = cur_r + dr[nd], cur_c + dc[nd]

        if nr < 0 or nc < 0 or N <= nr or M <= nc or MAP[nr][nc]:
            cur_d = nd    # 2-b. 왼쪽 방향에 청소할 공간이 없다면 그 방향으로 회전하고
            flag += 1
            continue    # 2번으로 돌아간다

        # 2-a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재하는 경우
        cur_d = nd    # 그 방향으로 회전한 다음
        cur = [nr, nc, cur_d]    # 한 칸을 전진하고 1번부터 반복
        break

    if flag == 4:
        # 2-c. 네 방향 모두 갈 수 없다면 방향을 유지한 채로 한 칸 후진
        nr, nc = cur_r - dr[cur_d], cur_c - dc[cur_d]
        cur = [nr, nc, cur_d]

        # 2-d. 만약 후진도 할 수 없는 경우에는 작동을 멈춘다
        if nr < 0 or nc < 0 or N <= nr or M <= nc or MAP[nr][nc] == 1:
            break

print(ans)
