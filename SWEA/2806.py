# 2806. N-Queen


def chess(row):
    global ans

    if row == N:  # 마지막 행에 도달하면 종료
        ans += 1
        return

    for col in range(N):
        if queen[col] or right_to_left[row + col] or left_to_right[col - row]:
            continue
        queen[col] = right_to_left[row + col] = left_to_right[col - row] = 1
        chess(row + 1)  # 다음 행으로 이동
        queen[col] = right_to_left[row + col] = left_to_right[col - row] = 0
    else:  # 퀸을 놓을 수 없는 경우
        return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    chess_board = [[0] * N for _ in range(N)]
    queen = [0] * N  # 퀸이 놓이는 체스판을 한 줄로 생각
    right_to_left = [0] * (2 * N + 1)  # 우측상단에서 좌측하단 대각선
    left_to_right = [0] * (2 * N + 1)  # 좌측상단에서 우측하단 대각선
    ans = 0  # 최종 정답
    chess(0)
    print(f'#{tc} {ans}')