# 2105. 디저트 카페


def dfs(row, col, direction):
    global start, ans

    for i in range(2):
        if i == 1 and direction == 3:
            continue  # direction == 4가 되는 경우 제외

        nr, nc = row + dr[direction + i], col + dc[direction + i]

        # 다음 디저트 가게 위치를 갈 수 있으면 간다
        if 0 <= nr < N and 0 <= nc < N:
            if nr == start[0] and nc == start[1]:  # 처음 위치 도착
                ans = max(ans, len(desserts))
                return

            if MAP[nr][nc] not in desserts:  # 다음 디저트가 없는 경우
                desserts.add(MAP[nr][nc])
                dfs(nr, nc, direction + i)
                desserts.remove(MAP[nr][nc])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    dr = [1, 1, -1, -1]  # 우하, 좌하, 좌상, 우상
    dc = [1, -1, -1, 1]

    ans = -1  # 최종 정답

    for r in range(N - 2):  # 0 <= row < N - 2
        for c in range(1, N - 1):  # 0 < col < N -1
            start = [r, c]  # 시작 위치
            desserts = set()  # 디저트 숫자를 담는 set
            desserts.add(MAP[r][c])
            dfs(r, c, 0)

    print(f'#{tc} {ans}')