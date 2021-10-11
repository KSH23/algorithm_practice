# 11048. 이동하기


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

# dp[r][c] == (r, c)에 도착할 때 얻을 수 있는 사탕의 최대 개수
dp = [[0] * (M + 1) for _ in range(N + 1)]

for r in range(1, N + 1):
    for c in range(1, M + 1):
        dp[r][c] = max(dp[r - 1][c - 1], dp[r][c - 1], dp[r - 1][c]) + MAP[r - 1][c - 1]

print(dp[N][M])