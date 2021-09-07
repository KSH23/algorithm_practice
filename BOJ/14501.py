# 14501. 퇴사


N = int(input())
T = [0] * (N+1)
P = [0] * (N+1)
for i in range(1, N + 1):
    T[i], P[i] = map(int, input().split())

dp = [0] * (N + 2)

for today in range(N, 0, -1):
    # case1 = dp[today + 1]    오늘 일 하지 않은 경우 벌 수 있는 돈
    # case2 = dp[today + T[today]] + P[today]    오늘 일 한 경우 벌 수 있는 돈

    # 문제는 case1과 case2중 최댓값을 dp[today]에 넣으면 되지만
    # 만약 today + T[today]가 N+1일 보다 크다면 일을 할 수 없으므로
    # 무조건 case1을 넣어야 한다

    if today + T[today] > N + 1:
        dp[today] = dp[today + 1]

    else:
        dp[today] = max(dp[today + 1], dp[today + T[today]] + P[today])


print(dp[1])


'''
처음 dp를 시도할 때에 생각한 경우
1. 오늘 일하는 경우
   1.1 오늘이 전에 일한 날과 곂치지 않는 경우
   1.2 오늘이 전에 일한 날과 곂치는 경우
2. 오늘을 일하지 않는 경우

기본적으로 오늘 일을 하는지, 하지 않는지에 따라 나뉜다는 감은 잡혔는데
일하는 날이 곂치는 경우때문에 1번을 다시 2개로 분리하고 꼬여버렸다.

심지어 dp 재귀 함수를 만들어 시도하는데 도저히 답이 나오지 않아
결국 검색을 해서 풀었다.
'''