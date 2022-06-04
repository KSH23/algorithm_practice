# 60061. 기둥과 보 설치


def solution(n, build_frame):
    frames = set()

    # [위쪽에 기둥의 존재 유무, 오른쪽에 보의 존재 유무]를 기록
    board = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]

    def check_board():
        # board를 검사해 규칙 만족 여부를 반환
        for r in range(n + 1):
            for c in range(n + 1):
                if board[r][c][0]:  # 기둥이 존재할 경우
                    if r == n or board[r + 1][c][0]:  # 바닥 또는 다른 기둥 위에 있는 경우
                        pass  # 보의 존재 여부도 검사하기 위해 continue 대신 pass
                    elif board[r][c][1] or (0 < c and board[r][c - 1][1]):  # 현재 위치 또는 좌측에 보가 있는 경우
                        pass
                    else:
                        return False
                if board[r][c][1]:  # 보가 존재할 경우
                    if board[r + 1][c][0] or (c < n and board[r + 1][c + 1][0]):  # 한쪽 끝에 기둥이 있는 경우
                        continue
                    elif 0 < c and board[r][c - 1][1] and board[r][c + 1][1]:  # 양쪽 끝이 보와 연결된 경우
                        continue
                    return False
        return True

    for col, row, frame, build in build_frame:
        row = n - row  # 문제와 같은 계산 편의를 위한 설정

        board[row][col][frame] = build  # 건설 또는 삭제
        if check_board():  # 규칙을 만족하는 경우
            if build:
                frames.add((col, n - row, frame))
            else:
                frames.discard((col, n - row, frame))
        else:  # 규칙을 만족하지 않는 경우 되돌림
            board[row][col][frame] = (build + 1) % 2

    return sorted(list([list(item) for item in list(frames)]))
