# 2579. 계단 오르기


import sys


N = int(sys.stdin.readline())
steps_cost = [int(sys.stdin.readline()) for _ in range(N)]

# [하나의 계단을 밟고 도착, 연속 두 개의 계단을 밟아 도착]
steps_dp = [[0, 0] for _ in range(N)]

for step in range(N):
    # 첫 번째, 두 번째 계단의 경우만 초기화가 필요
    if step == 0:
        steps_dp[step][0] = steps_cost[step]
        continue
    elif step == 1:
        steps_dp[step][0] = steps_cost[step]
        steps_dp[step][1] = steps_cost[step] + steps_cost[step - 1]
        continue

    # 연속으로 밟지 않는 경우
    steps_dp[step][0] = max(steps_dp[step - 2]) + steps_cost[step]

    # 연속으로 밟는 경우
    steps_dp[step][1] = steps_dp[step - 1][0] + steps_cost[step]

print(max(steps_dp[-1]))