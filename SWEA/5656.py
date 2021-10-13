# 5656. 벽돌 깨기


def count_bricks(board):
    # board에서 남은 벽돌의 개수를 세어 반환하는 함수
    cnt = 0
    for r in range(H):
        for c in range(W):
            if board[r][c]:
                cnt += 1
    return cnt


def rearrange(board):
    # 벽돌을 깬 이후에 board를 재정렬하는 함수

    stack = []  # 한 줄의 열에서 0이 아닌 수를 저장할 스택
    for col in range(W):
        for row in range(H):
            if board[row][col]:
                stack.append(board[row][col])

        # 스택에 담긴 숫자를 아래부터 다시 쌓아올림
        for row in range(H - 1, -1, -1):
            if len(stack) > 0:
                board[row][col] = stack.pop()
            else:  # 스택을 비우면 나머지는 0으로 채움
                board[row][col] = 0


def breaking(r, c, board):
    combo = board[r][c]  # 벽돌에 적힌 숫자
    board[r][c] = 0  # 벽돌 깸

    # 벽돌의 상하 처리
    for combo_r in range(r - combo + 1, r + combo):
        if combo_r < 0 or H <= combo_r:  # 판을 벗어나는 경우
            continue
        if board[combo_r][c] == 0:  # 벽돌이 없는 경우
            continue
        elif board[combo_r][c] == 1:  # 연쇄반응이 없는 경우
            board[combo_r][c] = 0
        else:
            breaking(combo_r, c, board)

    # 벽돌의 좌우 처리
    for combo_c in range(c - combo + 1, c + combo):
        if combo_c < 0 or W <= combo_c:  # 판을 벗어나는 경우
            continue
        if board[r][combo_c] == 0:  # 벽돌이 없는 경우
            continue
        elif board[r][combo_c] == 1:  # 연쇄반응이 없는 경우
            board[r][combo_c] = 0
        else:
            breaking(r, combo_c, board)


def pick_a_brick(n, initial_board):
    global ans

    if n == N:  # 벽돌을 N개 고른 경우
        ans = min(ans, count_bricks(initial_board))
        return

    for col in range(W):
        for row in range(H):
            if initial_board[row][col]:  # 벽돌을 만난 경우
                # 판을 deep copy해서 인자로 넘겨줌
                board_copy = [item[:] for item in initial_board]
                breaking(row, col, board_copy)  # 벽돌 깨기
                rearrange(board_copy)  # 판 재정렬
                pick_a_brick(n + 1, board_copy)  # 다음 벽돌 고르기
                break


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    BOARD = [list(map(int, input().split())) for _ in range(H)]
    ans = W * H + 1  # 최종 정답
    pick_a_brick(0, BOARD)

    # 최종 정답이 바뀌지 않은 경우는 N개의 벽돌을 고르기 전에 모든 벽돌이 꺠졌을 때
    if ans == W * H + 1:
        ans = 0

    print(f'#{tc} {ans}')