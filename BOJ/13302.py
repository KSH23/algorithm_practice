# 13302. 리조트


import sys


def dfs(d, coupon):
    min_cost = 10000 * N

    if d > N:
        return 0

    if dp[d][coupon] != 10000 * N:
        return dp[d][coupon]

    min_cost = min(min_cost, dfs(d + 1, coupon) + 10000)
    min_cost = min(min_cost, dfs(d + 3, coupon + 1) + 25000)
    min_cost = min(min_cost, dfs(d + 5, coupon + 2) + 37000)

    if coupon >= 3:
        min_cost = min(min_cost, dfs(d + 1, coupon - 3))

    if plan[d] == 0:
        min_cost = min(min_cost, dfs(d + 1, coupon))

    dp[d][coupon] = min_cost
    return min_cost


N, M = map(int, input().split())
plan = [0] + [1] * N
for day in list(map(int, sys.stdin.readline().split())):
    plan[day] = 0
dp = [[10000 * N] * (N + 6) for _ in range(N + 6)]


print(dfs(1, 0))