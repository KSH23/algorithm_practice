# 84021. 퍼즐 조각 채우기


from collections import deque, defaultdict


def rotate_block_180(block):
    # 블럭을 180도 회전시켜 반환
    row, col = len(block), len(block[0])
    rotate_180 = []
    for r in range(row):
        temp = []
        for c in range(col):
            temp.append(block[row - r - 1][col - c - 1])
        rotate_180.append(temp)

    return rotate_180


def rotate_block_90(block):
    # 블럭을 90도 회전시켜 반환
    row, col = len(block), len(block[0])
    rotate_90 = []
    for c in range(col):
        temp = []
        for r in range(row):
            temp.append(block[row - r - 1][c])
        rotate_90.append(temp)

    return rotate_90


def get_piece(r, c, board, visited, mark):
    # 블럭 또는 빈 공간을 방문표시한 뒤 조각 개수와 함께 반환
    n = len(board)
    min_r, max_r, min_c, max_c = n, -1, n, -1  # 차지하는 크기의 경계선
    count = 0  # 조각 개수

    # BFS
    dr, dc = [-1, 0, 1, 0], [0, -1, 0, 1]  # 상좌하우
    dq = deque([(r, c)])
    while dq:
        cr, cc = dq.popleft()
        min_r, max_r = min(min_r, cr), max(max_r, cr)
        min_c, max_c = min(min_c, cc), max(max_c, cc)
        count += 1
        for nd in range(4):
            nr, nc = cr + dr[nd], cc + dc[nd]
            if nr < 0 or nc < 0 or n <= nr or n <= nc:
                continue
            if board[nr][nc] != board[r][c] or visited[nr][nc] == mark:
                continue

            # 방문 표시를 블럭마다 다르게 하여 직사각형에 다른 블럭이 포함되지 않도록 설정
            visited[nr][nc] = mark
            dq.append((nr, nc))

    # 최소 크기 직사각형에 블럭 또는 빈 공간을 표시
    block = [[(board[r][c] + 1) % 2] * (max_c - min_c + 1) for _ in range(max_r - min_r + 1)]
    for row in range(max_r - min_r + 1):
        for col in range(max_c - min_c + 1):
            if visited[min_r + row][min_c + col] == mark:
                block[row][col] = board[r][c]

    return block, count


def check_block(place, block):
    # 게임 판에 블록이 들어갈 수 있는지 여부를 반환
    for row in range(len(block)):
        for col in range(len(block[0])):
            if place[row][col] + block[row][col] != 1:
                return False
    return True


def solution(game_board, table):
    n = len(game_board)
    blocks = defaultdict(list)  # (세로 길이, 가로 길이)를 key, 크기에 해당하는 block을 value로 가짐
    visited_table = [[0] * n for _ in range(n)]  # table의 방문 여부 기록
    visited_game_board = [[0] * n for _ in range(n)]  # game_board의 방문 여부 기록

    mark = 1  # 블럭과 빈 공간에 부여될 고유한 숫자
    for row in range(n):
        for col in range(n):
            if table[row][col] and visited_table[row][col] == 0:
                visited_table[row][col] = mark  # 블럭을 발견한 경우 방문 표시

                # 블럭을 딱맞게 포함하는 직사각형 행렬을 딕셔너리에 저장
                block, _ = get_piece(row, col, table, visited_table, mark)
                blocks[(len(block), len(block[0]))].append(block)
                mark += 1

    answer = 0
    for row in range(n):
        for col in range(n):
            if game_board[row][col] == 0 and visited_game_board[row][col] == 0:
                visited_game_board[row][col] = mark  # 빈 공간을 발견한 경우 방문 표시

                # 빈 공간과 조각의 개수
                place, count = get_piece(row, col, game_board, visited_game_board, mark)
                row_length, col_length = len(place), len(place[0])

                # 크기가 일치하는 블럭중 빈 공간과 일치하는 경우 검사
                for _ in range(len(blocks[(row_length, col_length)])):
                    block = blocks[(row_length, col_length)].pop()
                    # 180도 회전한 블럭에 대해서도 검사
                    if check_block(place, block) or check_block(place, rotate_block_180(block)):
                        answer += count
                        break
                    blocks[(row_length, col_length)] = [block] + blocks[(row_length, col_length)]

                else:  # 90도 회전한 경우 크기가 맞는 블럭을 가져와 빈 공간에 맞는지 검사
                    for _ in range(len(blocks[(col_length, row_length)])):
                        block = blocks[(col_length, row_length)].pop()
                        rotated_block = rotate_block_90(block)
                        # 180도 회전한 블럭에 대해서도 검사
                        if check_block(place, rotated_block) or check_block(place, rotate_block_180(rotated_block)):
                            answer += count
                            break
                        blocks[(col_length, row_length)] = [block] + blocks[(col_length, row_length)]

                mark += 1

    return answer
