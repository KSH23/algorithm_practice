# 1562. 계단 수


N = int(input())

# dp[length][end_num][bit]: 길이가 length이며 end_num으로 끝나는 수의 개수
# 그 중 0 ~ 9까지 어떤 수가 들어있는지 비트로 표시
dp = [[[0] * 1024 for _ in range(10)] for _ in range(N + 1)]

# 한자리 숫자 초기화
for end_num in range(1, 10):
    dp[1][end_num][1 << end_num] = 1

for length in range(1, N):
    for end_num in range(10):
        # 현재 끝나는 수 뒤에 추가할 수 있는 숫자를 검사하고 해당 숫자가 추가됨을 비트 연산으로 표현
        for bit in range(1024):
            # 현재 숫자의 뒤에 (end_num + 1) 숫자를 붙일 수 있는 경우
            # 즉 10이 오는 경우를 제외하고 경우의 수 증가
            if end_num + 1 <= 9:
                dp[length + 1][end_num + 1][bit | 1 << (end_num + 1)] += dp[length][end_num][bit]

            # 현재 숫자의 뒤에 (end_num - 1) 숫자를 붙일 수 있는 경우
            # 즉 -1이 오는 경우를 제외하고 경우의 수 증가
            if 0 <= end_num - 1:
                dp[length + 1][end_num - 1][bit | 1 << (end_num - 1)] += dp[length][end_num][bit]

ans = 0
for end_num in range(10):
    # 0 ~ 9 까지 모든 숫자가 포함된 즉, 비트가 1023을 나타내는 수만 고려
    ans += dp[N][end_num][1023]
print(ans % 1000000000)