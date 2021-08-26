# 1210. Ladder1(델타검색 이용)


def ladder_winner(ladder):
    col, row = 0, 99

    # 2가 적힌곳의 행을 알아내 변수에 저장
    for i in range(100):
        if ladder[99][i] == 2:
            col = i

    di = [-1, 0, 0]    # 상 좌 우
    dj = [0, -1, 1]    # 상 좌 우
    pre = 0    # 이전에 온 방향

    while row != 0:
        for k in range(3):
            # 좌에서 오다가 우로 가는 경우 또는 우에서 오다가 좌로 가는 경우 무시
            if pre + k == 3:
                continue

            nr = row + di[k]
            nc = col + dj[k]
            if nr < 0 or 100 <= nr or nc < 0 or 100 <= nc:
                continue
            if MAP[nr][nc] == 0:
                continue

            row = nr
            col = nc
            pre = k    # 현재 가는 방향 저장

    return col


T = 10
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(100)]

    print(f'#{tc} {ladder_winner(MAP)}')