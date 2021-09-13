# 2001. 파리 퇴치(dp 사용)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    MAP = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + MAP[i][j]

    ans = dp[1][1]
    for i in range(M, N + 1):
        for j in range(M, N + 1):
            flies = dp[i][j] - dp[i - M][j] - dp[i][j - M] + dp[i - M][j - M]
            if flies > ans:
                ans = flies

    print('#{} {}'.format(tc, ans))