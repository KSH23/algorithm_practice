# 10803. 정사각형 만들기


def cut_paper(row, col):
    if dp[row][col]:  # 이미 계산한 경우
        return dp[row][col]

    if row == col:  # 정사각형의 경우
        dp[row][col] = 1
        dp[col][row] = 1
        return dp[row][col]

    if row == 1 or col == 1:  # 한 줄 사각형
        dp[row][col] = max(row, col)
        if col <= max_len and row <= min_len:
            dp[col][row] = dp[row][col]
        return dp[row][col]

    # 정사각형의 일직선 배열
    if row % col == 0:
        dp[row][col] = row // col
        if col <= max_len and row <= min_len:
            dp[col][row] = dp[row][col]
        return dp[row][col]
    if col % row == 0:
        dp[row][col] = col // row
        if col <= max_len and row <= min_len:
            dp[col][row] = dp[row][col]
        return dp[row][col]

    result = row * col
    if row >= col * 3:  # 종이 비율의 차이가 심하면 (row // (col * 3))개씩 잘라냄
        result = min(result, cut_paper(row - col * (row // (col * 3)), col) + row // (col * 3))

    else:  # row와 col을 기준으로 한 칸씩 잘라냄
        for cutting_col in range(1, col // 2 + 1):
            result = min(result, cut_paper(row, col - cutting_col) + cut_paper(row, cutting_col))
        for cutting_row in range(1, row // 2 + 1):
            result = min(result, cut_paper(row - cutting_row, col) + cut_paper(cutting_row, col))

    dp[row][col] = result
    if col <= max_len and row <= min_len:
        dp[col][row] = dp[row][col]
    return result


n, m = map(int, input().split())
max_len, min_len = max(n, m), min(n, m)
dp = [[0] * (min_len + 1) for _ in range(max_len + 1)]
print(cut_paper(max_len, min_len))  # row가 col보다 크게 설정하고 함수 실행