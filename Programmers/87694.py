# 87694. 아이템 줍기


def solution(rectangle, character_x, character_y, item_x, item_y):
    # 두 변이 한 칸 떨어져있는 경우 맞닿아있는 것 처럼 인식하지 않도록 좌표 값을 2배로 늘림
    character_x, character_y = character_x * 2, character_y * 2
    item_x, item_y = item_x * 2, item_y * 2
    board = [[0] * 102 for _ in range(102)]  # 좌표 평면

    start_x, start_y = 102, 102  # 출발 지점
    for rec in rectangle:
        left_bottom_x, left_bottom_y, right_top_x, right_top_y = [item * 2 for item in rec]

        # 출발 지점을 최좌측하단으로 설정해 이후 왼쪽으로만 돌아 최외각을 움직일 예정
        # 출발 지점을 따로 설정하여 초기 이동 방향을 상으로 고정할 수 있음
        if left_bottom_x < start_x:
            start_x, start_y = left_bottom_x, left_bottom_y

        # 직사각형의 테두리를 좌표 평면에 1로 기록
        for x in range(left_bottom_x, right_top_x + 1):
            board[x][left_bottom_y] = 1
            board[x][right_top_y] = 1
        for y in range(left_bottom_y, right_top_y + 1):
            board[left_bottom_x][y] = 1
            board[right_top_x][y] = 1

    dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]  # 다음 방향이 왼쪽이 되도록 상좌우하로 설정

    x, y, direction = start_x, start_y + 1, 0  # 현재 위치와 방향
    total_route, item_route = 1, 0  # 총 거리, 캐릭터와 아이템 사이 거리
    hit = False  # 캐릭터 또는 아이템을 한 번만 만난 경우 True
    while x != start_x or y != start_y:
        # 최외각만 돌기 위해 왼쪽에 길이 있다면 무조건 먼저 왼쪽으로 가고
        # 왔던 방향((direction + 2) % 4)으로는 되돌아 가지 않음
        for d in [(direction + 1) % 4, (direction + 3) % 4, direction]:
            nx, ny = x + dx[d], y + dy[d]  # 다음 위치
            if board[nx][ny]:  # 움직일 수 있는 경우
                x, y, direction = nx, ny, d

                total_route += 1  # 총 거리 갱신
                if hit:
                    item_route += 1  # 캐릭터와 아이템 사이 거리 갱신

                # 캐릭터 또는 아이템의 만남 여부 갱신
                if (x == character_x and y == character_y) or (x == item_x and y == item_y):
                    hit = not hit

                break

    return min(item_route, total_route - item_route) // 2
