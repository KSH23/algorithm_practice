# 11559. Puyo Puyo


def find_puyo(cur_r, cur_c):    # 기본 BFS 이용
    di = [-1, 1, 0, 0]    # 상하좌우
    dj = [0, 0, -1, 1]

    visited = [[0] * 6 for _ in range(12)]
    visited[cur_r][cur_c] = 1
    Q = [(cur_r, cur_c)]    # 큐 생성

    cnt = 1    # 같은 색 갯수
    while len(Q) > 0:
        now = Q.pop(0)
        now_r, now_c = now[0], now[1]

        for k in range(4):
            nr, nc = now_r + di[k], now_c + dj[k]

            if nc < 0 or 6 <= nc or nr < 0 or 12 <= nr:
                continue
            if visited[nr][nc] > 0:
                continue
            if field[nr][nc] != field[now_r][now_c]:
                continue

            visited[nr][nc] = visited[now_r][now_c] + 1
            cnt += 1
            Q.append((nr, nc))

    if cnt >= 4:    # 만약 같은 색이 4개 이상이라면
        for i in range(12):    # 모든 행과
            for j in range(6):    # 모든 열에 대해서
                if visited[i][j] > 0:    # 방문한 적 있는 칸의
                    field[i][j] = '.'    # 색 터트림

        return 1    # 뿌요 터졌으니 1 반환

    return 0    # 뿌요가 터지지 않았다면 0 반환


def rearrange():    # 뿌요뿌요판 재정렬 함수
    for col in range(6):    # 여섯 개의 세로줄에서 반복
        temp = []    # 뿌요가 터진 상태에서의 세로줄을 담는 임시 리스트
        for row in range(11, -1, -1):
            temp += field[row][col]    # 뿌요가 터진 상태의 세로줄 추가

        row_idx = 11    # 가로 인덱스는 맨 아래부터 시작
        for item in temp:
            if item == '.':    # 리스트의 원소가 색깔이 아니면 넘어감
                continue

            # 리스트의 원소가 색깔이라면 뿌요뿌요판에 밑에서부터 변경
            field[row_idx][col] = item
            row_idx -= 1    # 다음 색깔은 한 칸 위에 오도록 변수 수정

        if row_idx > -1:    # 만약 가로 인덱스가 -1에 도달하지 못했다면
            for r in range(row_idx, -1, -1):
                field[r][col] = '.'    # 남은 세로칸은 모두 . 으로 채움


field = [list(input()) for _ in range(12)]    # 뿌요뿌요 판
ans = 0    # 연쇄 횟수를 담는 최종 정답 변수

while True:
    puyo_cnt = 0    # 이번 while에서 뿌요를 한 횟수
    for i in range(12):
        for j in range(6):
            if field[i][j] != '.':    # 색깔을 만나면 find_puyo 실행
                puyo_cnt += find_puyo(i, j)

    if puyo_cnt > 0:    # 만약 뿌요가 한번이라도 터졌다면
        rearrange()    # 뿌요뿌요판 재정렬
        ans += 1    # 최종 답에 1 증가
    else:    # 뿌요가 한 번도 터지지 못했다면
        break    # 게임 끝

print(ans)