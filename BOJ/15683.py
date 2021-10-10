# 15683. 감시


import sys


def surveillance(idx, cnt, visited):  # 감시할 수 있는 영역 수를 반환하는 함수
    # idx: 현재 CCTV의 인덱스
    # cnt: 현재 감시중인 영역 개수
    # visited: 현재 감시중인 사무실의 2차원 리스트

    global ans

    if blind_cnt < cnt:  # 모든 영역을 전부 감시하는 경우
        ans = 0
        return

    if idx == len(CCTV_list):  # 모든 CCTV를 전부 실행한 경우
        ans = min(ans, blind_cnt - cnt)  # 최종 정답 갱신
        return

    row, col = CCTV_list[idx][0], CCTV_list[idx][1]  # 현재 CCTV의 좌표
    now = CCTV_list[idx][2]  # 현재 CCTV의 번호(1번 ~ 5번)

    for turn in range(len(dr[now])):  # turn: 현재 CCTV가 설치된 방법
        visited_copy = [item[:] for item in visited]  # 사무실 2차원 배열 깊은 복사
        cnt_copy = cnt
        if visited_copy[row][col] != 7:  # 현재 CCTV 좌표 확인이 되어있지 않은 경우
            cnt_copy += 1
            visited_copy[row][col] = 7

        for d in range(len(dr[now][turn])):  # d: 현재 CCTV가 보는 방향
            distance = 1  # CCTV가 감시하는 거리

            # 벽에 닿을 때 까지 CCTV가 감시할 수 있는 구역을 표시
            while True:
                nr = row + dr[now][turn][d] * distance
                nc = col + dc[now][turn][d] * distance

                if nr < 0 or nc < 0 or R <= nr or C <= nc:
                    break
                if office[nr][nc] == 6:
                    break
                if visited_copy[nr][nc] == 7:
                    distance += 1
                    continue

                cnt_copy += 1
                visited_copy[nr][nc] = 7
                distance += 1

        surveillance(idx + 1, cnt_copy, visited_copy)


R, C = map(int, input().split())
CCTV_list = []  # CCTV 좌표 저장 리스트
office = []  # 사무실
blind_cnt = 0  # 사각 지대 개수
for r in range(R):
    temp = list(map(int, sys.stdin.readline().split()))
    for c in range(C):
        if 1 <= temp[c] <= 5:
            CCTV_list.append([r, c, temp[c]])
        elif temp[c] == 0:
            blind_cnt += 1
    office.append(temp)

# 감시 방향의 델타 좌표 인덱스 == CCTV의 번호
# 2번: 상하, 좌우 / 3번: 상우, 우하, 하좌, 좌상 / 4번: 상좌우, 상하우, 하좌우, 상하좌
dr = [[], [[-1], [1], [0], [0]],
      [[-1, 1], [0, 0]],
      [[-1, 0], [0, 1], [1, 0], [0, -1]],
      [[-1, 0, 0], [-1, 1, 0], [1, 0, 0], [-1, 1, 0]],
      [[-1, 1, 0, 0]]]
dc = [[], [[0], [0], [-1], [1]],
      [[0, 0], [-1, 1]],
      [[0, 1], [1, 0], [0, -1], [-1, 0]],
      [[0, -1, 1], [0, 0, 1], [0, -1, 1], [0, 0, -1]],
      [[0, 0, -1, 1]]]

initial_visited = [[0] * C for _ in range(R)]  # 초기 visited 배열
blind_cnt += len(CCTV_list)  # 이후 CCTV 위치도 뺄 예정이므로 이를 보정
ans = blind_cnt  # 최종 정답
surveillance(0, 0, initial_visited)
print(ans)