# 11727. 2×n 타일링 2


N = int(input())
dp = [0] * (N + 1)

for i in range(1, N + 1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 3
    else:
        dp[i] = 2 * dp[i - 2] + dp[i - 1]

print(dp[N] % 10007)