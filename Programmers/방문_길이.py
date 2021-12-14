# 방문 길이
# https://programmers.co.kr/learn/courses/30/lessons/49994


def solution(dirs):
    answer = 0
    # 게임 지도의 각 칸과 칸 사이를 포함하여 2차원 배열 설정
    game_map = [[False] * 22 for _ in range(22)]

    # 방향과 인덱스 연결
    dir_idx = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

    dr = (-1, 1, 0, 0)  # 상하좌우 행 델타
    dc = (0, 0, -1, 1)  # 상하좌우 열 델타

    cur_row, cur_col = 10, 10  # 현재 위치
    for dir in dirs:
        next_dir = dir_idx[dir]  # 다음 방향의 인덱스
        between_row, between_col = cur_row + dr[next_dir], cur_col + dc[next_dir]
        next_row, next_col = cur_row + 2 * dr[next_dir], cur_col + 2 * dc[next_dir]

        # 범위를 벗어나는 경우
        if next_row < 0 or 21 < next_row or next_col < 0 or 21 < next_col:
            continue

        # 해당 길을 처음 지나는 경우
        if not game_map[between_row][between_col]:
            answer += 1
            game_map[between_row][between_col] = True  # 방문 표시

        cur_row, cur_col = next_row, next_col  # 이동

    return answer