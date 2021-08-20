# 4869. 종이붙이기


T = int(input())
dp = [0, 1, 3]
for tc in range(1, T+1):
    N = int(input()) // 10

    if N >= len(dp):
        for i in range(len(dp), N+1):
            dp += [dp[i -1] + 2 * dp[i - 2]]

    print('#{} {}'.format(tc, dp[N]))