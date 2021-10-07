# 1861. 정사각형 방


def dfs(row, col):
    if 0 <= dp[row][col]:
        return dp[row][col]

    result = 0
    for d in range(4):
        nr, nc = row + dr[d], col + dc[d]
        if nr < 0 or nc < 0 or N <= nr or N <= nc:
            continue
        if MAP[row][col] + 1 == MAP[nr][nc]:
            result = max(result, dfs(nr, nc) + 1)

    dp[row][col] = result
    return result


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    # dp[r][c]: (r, c)에서 갈 수 있는 최장 경로
    dp = [[-1] * N for _ in range(N)]

    dr = [-1, 1, 0, 0]  # 동서남북
    dc = [0, 0, -1, 1]

    ans = 0  # 최장 경로
    ans_numbers = N * N  # 최장 경로 시작점에 적힌 숫자

    for r in range(N):
        for c in range(N):
            temp = dfs(r, c)  # 경로 계산
            if ans < temp:
                ans = temp
                ans_numbers = MAP[r][c]
            if ans == temp and MAP[r][c] < ans_numbers:
                ans_numbers = MAP[r][c]

    print(f'#{tc} {ans_numbers} {ans + 1}')