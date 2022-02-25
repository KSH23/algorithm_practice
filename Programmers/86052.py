# 86052. 빛의 경로 사이클


def solution(grid):
    answer = []
    row, col = len(grid), len(grid[0])

    # 해당 칸으로 도착하는 빛이 있는지 표시하기 위한 배열
    route = [[[0, 0, 0, 0] for _ in range(col)] for _ in range(row)]

    dr = (-1, 0, 1, 0)  # 상우하좌 시계방향 행
    dc = (0, 1, 0, -1)  # 상우하좌 시계방향 열
    dir_dict = {"S": 0, "L": -1, "R": 1}  # grid에 적힌 문자에 따른 방향 전환

    # 빛의 현재 위치에 방문 표시를 하고 다음 좌표를 반환하는 함수
    def move(current_row, current_col, direction):
        # 사이클이 생긴 경우 도달할 수 없는 값을 반환
        if route[current_row][current_col][direction]:
            return row, row, row

        route[current_row][current_col][direction] = 1  # 방문 표시

        # grid에 적힌 문자에 따른 방향 전환 적용
        direction = (direction + dir_dict[grid[current_row][current_col]]) % 4

        # 다음 좌표
        next_row = (current_row + dr[direction]) % row
        next_col = (current_col + dc[direction]) % col

        return next_row, next_col, direction

    for r in range(row):
        for c in range(col):
            for d in range(4):
                # (r, c)에서 d 방향으로 빛을 쏘았을 때 다음 좌표를 현재 좌표로 저장
                cur_r, cur_c, cur_d = (r + dr[d]) % row, (c + dc[d]) % col, d

                # 만약 현재 좌표에 이미 도달한 적 있다면 무시
                if route[cur_r][cur_c][cur_d]:
                    continue

                cnt = 0  # 빛의 경로 사이클 길이
                while cur_r < row:
                    # 다음 좌표를 현재 좌표에 갱신한 뒤 cnt 증가
                    cur_r, cur_c, cur_d = move(cur_r, cur_c, cur_d)
                    cnt += 1

                # 사이클이 생겨 빠져나오는 순간 cnt가 1 추가되고 나오기 때문에
                # 답은 cnt에서 1을 빼야 함
                answer.append(cnt - 1)

    answer.sort()  # 오름차순 정렬
    return answer
