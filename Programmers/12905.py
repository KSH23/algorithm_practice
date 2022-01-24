# 12905. 가장 큰 정사각형 찾기


def solution(board):
    answer = 0
    row, col = len(board), len(board[0])  # 표의 행과 열

    # 계산의 편의를 위해 상단과 좌측에 0으로 구성된 한 줄의 리스트 추가
    for r in range(row):
        board[r] = [0] + board[r]
    board = [[0] * (col + 1)] + board

    # check_board[x, y, z]
    # x: 현재 위치에서 좌측에 있는 연속된 1의 개수(현재 위치 포함)
    # z: 현재 위치에서 상단에 있는 연속된 1의 개수(현재 위치 포함)
    # y: 현재 위치를 우측 하단 꼭지점으로 갖는 정사각형의 변의 길이 저장
    check_board = [[[0, 0, 0] for _ in range(col + 1)] for _ in range(row + 1)]

    for r in range(row + 1):
        for c in range(col + 1):
            if not board[r][c]:  # 0인 경우 무시
                continue

            # 현재 위치에서 좌측에 있는 연속된 1의 개수(현재 위치 포함)
            check_board[r][c][0] = check_board[r][c - 1][0] + 1
            # 현재 위치에서 상단에 있는 연속된 1의 개수(현재 위치 포함)
            check_board[r][c][2] = check_board[r - 1][c][2] + 1

            # 현재 위치를 우측 하단 꼭지점으로 갖는 정사각형의 변의 길이는
            # (현재 위치의 좌측 상단을 꼭지점으로 갖는 정사각형의 변의 길이 + 1)과
            # 현재 위치에서 좌측과 상단으로 뻗어나갈 수 있는 연속된 1의 개수 중 최솟값
            check_board[r][c][1] = min(check_board[r - 1][c - 1][1] + 1, check_board[r][c][0], check_board[r][c][2])

            answer = max(answer, check_board[r][c][1])  # 최댓값으로 정답 갱신

    return answer ** 2