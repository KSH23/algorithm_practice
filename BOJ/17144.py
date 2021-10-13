# 17144. 미세먼지 안녕!


import sys


def diffuse():
    global room, purifier_coord

    room_copy = [[0] * C for _ in range(R)]  # 확산 이후 방
    for r in range(R):
        for c in range(C):
            if room[r][c] == 0:  # 미세먼지가 없는 곳
                continue
            elif room[r][c] == -1:  # 공기청정기가 설치된 위치
                room_copy[r][c] = -1  # 공기청정기 표시
                purifier_coord.append([r, c])
                continue

            cnt = 0  # 확산된 방향의 개수
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]  # 확산될 다음 칸
                if nr < 0 or nc < 0 or R <= nr or C <= nc:
                    continue
                if room[nr][nc] == -1:  # 공기청정기 위치
                    continue
                cnt += 1
                room_copy[nr][nc] += room[r][c] // 5
            room_copy[r][c] += room[r][c] - (room[r][c] // 5) * cnt

    room = room_copy  # 방의 미세먼지 갱신


def drift():
    up = purifier_coord[0]  # 위쪽 공기청정기의 좌표
    down = purifier_coord[1]  # 아래쪽 공기청정기의 좌표

    up_row, up_col = up[0] - 1, up[1]  # 위쪽 공기 순환 시작점
    down_row, down_col = down[0] + 1, down[1]  # 아래쪽 공기 순환 시작점

    drift_dr = [1, 0, -1, 0]  # 하향, 좌향, 상향, 우향 행
    drift_dc = [0, -1, 0, 1]  # 하향, 좌향, 상향, 우향 열

    for d in range(4):
        # 현재 방향에서 한 칸 뒤를 갈 수 있다면 한칸 뒤와 현재 위치를 교환하고
        # 이후 현재 위치를 한 칸 뒤로 민다
        while 0 <= up_row - drift_dr[d] <= up[0] and 0 <= up_col - drift_dc[d] < C:
            room[up_row][up_col] = room[up_row - drift_dr[d]][up_col - drift_dc[d]]
            up_row -= drift_dr[d]
            up_col -= drift_dc[d]

        while down[0] <= down_row + drift_dr[d] < R and 0 <= down_col - drift_dc[d] < C:
            room[down_row][down_col] = room[down_row + drift_dr[d]][down_col - drift_dc[d]]
            down_row += drift_dr[d]
            down_col -= drift_dc[d]

    room[up[0]][up[1] + 1] = 0  # 공기청정기에 들어간 미세먼지
    room[down[0]][down[1] + 1] = 0  # 공기청정기에 들어간 미세먼지


R, C, T = map(int, input().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

dr = [-1, 1, 0, 0]  # 상하좌우 행
dc = [0, 0, -1, 1]  # 상하좌우 열

purifier_coord = []  # 공기청정기 위치
for _ in range(T):
    diffuse()  # 확산
    drift()  # 이동

ans = 0  # 최종 정답
for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            ans += room[i][j]
print(ans)