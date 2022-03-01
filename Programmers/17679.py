# 17679. [1차] 프렌즈4블록


def remove_block(m, n, board):
    blocks = set()  # 지워질 블록의 위치를 기록할 세트
    dr = (0, 1, 1)  # 행의 우, 하, 우하
    dc = (1, 0, 1)  # 열의 우, 하, 우하

    for row in range(m - 1):
        for col in range(n - 1):
            if not board[row][col]:  # 블록이 없는 경우
                continue

            for d in range(3):  # 4블록 검사
                if board[row][col] != board[row + dr[d]][col + dc[d]]:
                    break

            else:  # 4블록을 마주한 경우 네 개의 블록 위치를 저장
                blocks.add((row, col))
                for d in range(3):
                    blocks.add((row + dr[d], col + dc[d]))

    for row, col in blocks:  # 블록 지우기
        board[row][col] = ""

    return len(blocks), board


def align_blocks(m, n, board):
    for col in range(n):
        column = []  # 하나의 열

        # 열을 맨 아래 행부터 탐색하여 블록만 저장한 뒤 남은 길이는 빈 문자열로 채움
        for row in range(m - 1, -1, -1):
            if board[row][col]:
                column.append(board[row][col])
        column += ["" for _ in range(m - len(column))]

        # 기존의 열을 정렬된 열로 바꾸기
        for row in range(m - 1, -1, -1):
            board[row][col] = column[m - 1 - row]

    return board


def solution(m, n, board):
    answer = 0

    board = [list(board[row]) for row in range(m)]
    while True:
        # 지워진 블록의 개수와 블록이 지워진 후의 판
        removed, board = remove_block(m, n, board)

        if removed == 0:  # 게임 종료
            return answer

        answer += removed
        align_blocks(m, n, board)  # 판 재정렬
