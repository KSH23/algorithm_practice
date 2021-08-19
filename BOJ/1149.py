# 1149. RGB거리


def MIN(li):    # 리스트를 받으면 그 중 가장 작은 원소 반환
    result = li[0]
    for i in range(len(li)):
        if result > li[i]:
            result = li[i]

    return result


N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0] = house[0]

for i in range(1, N):
    # 현재 집에 칠 할 수 있는 경우의 수를 dp 리스트에 채워 넣음
    dp[i][0] = MIN([dp[i-1][1], dp[i-1][2]]) + house[i][0]
    dp[i][1] = MIN([dp[i-1][0], dp[i-1][2]]) + house[i][1]
    dp[i][2] = MIN([dp[i-1][1], dp[i-1][0]]) + house[i][2]

print(MIN(dp[N-1]))    # 가장 최소값이 최종 결과
