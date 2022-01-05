# 10844. 쉬운 계단 수


N = int(input())

# dp[length][end_num]: 길이가 length이며 end_num으로 끝나는 수의 개수
dp = [[0] * 10 for _ in range(N + 1)]
dp[1] = [0] + [1] * 9  # 한자리 숫자 초기화

for length in range(1, N):
    for end_num in range(10):
        # 현재 숫자의 뒤에 (end_num + 1) 숫자를 붙일 수 있는 경우
        # 즉 10이 오는 경우를 제외하고 경우의 수 증가
        if end_num + 1 <= 9:
            dp[length + 1][end_num + 1] += dp[length][end_num]

        # 현재 숫자의 뒤에 (end_num - 1) 숫자를 붙일 수 있는 경우
        # 즉 -1이 오는 경우를 제외하고 경우의 수 증가
        if 0 <= end_num - 1:
            dp[length + 1][end_num - 1] += dp[length][end_num]

print(sum(dp[N]) % 1000000000)