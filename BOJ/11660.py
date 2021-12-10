# 11660. 구간 합 구하기 5


import sys


N, M = map(int, sys.stdin.readline().split())

# 계산의 편의를 위해 상단, 좌측에 빈 리스트 추가
MAP = [[0] * (N + 1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# (1, 1)에서 (row, col)까지의 구간 합 저장
dp = [[0] * (N + 1) for _ in range(N + 1)]
for row in range(1, N + 1):
    for col in range(1, N + 1):
        dp[row][col] = dp[row - 1][col] + dp[row][col - 1] - dp[row - 1][col - 1] + MAP[row][col]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])