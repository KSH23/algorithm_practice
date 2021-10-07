# 5208. 전기버스2


def dfs(now, cnt):
    global ans

    dp[now] = cnt

    if now == N - 1:  # 끝까지 도달
        if cnt < ans:
            ans = cnt  # 최솟값 갱신
        return

    for i in range(now + 1, now + batteries[now] + 1):
        if N <= i:
            continue  # 다음 좌표가 N 이상이면 갈 필요 없음
        if 0 <= dp[i] < cnt + 1:
            continue  # 다음 좌표 dp 값이 더 작으면 갈 필요 없음
        dfs(i, cnt + 1)


T = int(input())
for tc in range(1, T + 1):
    temp = list(map(int, input().split()))
    N = temp[0]
    batteries = temp[1:]
    dp = [-1] * N  # dp[i]: i까지 갈 수 있는 최소 경우의 수
    ans = 100  # 최종 정답
    dfs(0, -1)
    print(f'#{tc} {ans}')