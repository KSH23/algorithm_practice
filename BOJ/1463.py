# 1463 1로 만들기


N = int(input())
dp = [0] * (N + 1)

for num in range(2, N+1):
    if num % 2 == 0 and num % 3 == 0:
        dp[num] = min(dp[num - 1], dp[num // 2], dp[num // 3]) + 1
    elif num % 2 == 0:
        dp[num] = min(dp[num - 1], dp[num // 2]) + 1
    elif num % 3 == 0:
        dp[num] = min(dp[num - 1], dp[num // 3]) + 1
    else:
        dp[num] = dp[num - 1] + 1

print(dp[N])