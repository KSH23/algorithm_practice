# 9095. 1, 2, 3 더하기


T = int(input())
for _ in range(T):
    N = int(input())
    ans = 0  # 최종 정답
    dp = [0] * (N + 1)  # dp[i]: i를 만들 수 있는 방법의 수

    for num in range(1, N + 1):
        # 1, 2, 3을 제외하면 나머지 수를 만드는 방법의 수는
        # 한 칸, 두 칸, 세 칸을 제거한 수들의 방법의 총 합
        if num < 3:
            dp[num] = num
            continue

        if num == 3:
            dp[num] = 4
            continue

        dp[num] = dp[num - 1] + dp[num - 2] + dp[num - 3]

    print(dp[N])