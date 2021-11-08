# 11726. 2×n 타일링


N = int(input())
dp = [0] * (N + 1)

# 2xn 크기의 직사각형을 채우는 방법의 수는
# 2x(n-1) 크기의 직사각형, 2x(n-2) 크기의 직사각형을 채우는 방법의 수의 합
for i in range(N + 1):
    if i < 3:
        dp[i] = i
    else:
        dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N] % 10007)