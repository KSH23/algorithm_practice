# 9663. N-Queen


def chess(row):
    global ans
    
    if row == N:  # 마지막 행에 도달하면 종료
        ans += 1
        return

    possible_col = [-1] * N  # 퀸이 갈 수 있는 열
    for idx in range(row):
        # case1-3은 퀸이 갈 수 없는 열
        case1 = queen[idx] - (row - idx)
        case2 = queen[idx] + (row - idx)
        case3 = queen[idx]
        
        # 퀸이 갈 수 없는 열을 1로 ㅍ시
        if 0 <= case1:
            possible_col[case1] = 1
        if case2 < N:
            possible_col[case2] = 1
        possible_col[case3] = 1

    for idx in range(N):
        # 퀸이 갈 수 있는 열은 -1로 표시되어 있음
        if possible_col[idx] == -1:
            queen[row] = idx  # 퀸을 놓음
            chess(row + 1)  # 다음 행으로 이동
            queen[row] = -1  # 퀸을 뺌
    else:  # 퀸을 놓을 수 없는 경우
        return


N = int(input())
chess_board = [[0] * N for _ in range(N)]
queen = [-1] * N  # 퀸이 놓이는 체스판을 한 줄로 생각
ans = 0  # 최종 정답
chess(0)
print(ans)