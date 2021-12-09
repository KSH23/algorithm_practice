# 9465. 스티커


import sys


sys.setrecursionlimit(200000)


def sticker(current_row, current_col):
    if N <= current_col:  # 범위 밖
        return 0

    if -1 < dp[current_row][current_col]:  # 이미 계산한 경우
        return dp[current_row][current_col]

    # 현재 row에서 스티커를 제거하는 경우
    result = sticker((current_row + 1) % 2, current_col + 1) + MAP[current_row][current_col]

    # 현재 row를 건너뛰고 그 다음 row에서 스티커를 제거하는 경우
    result = max(result, sticker(0, current_col + 2) + MAP[current_row][current_col])
    result = max(result, sticker(1, current_col + 2) + MAP[current_row][current_col])

    dp[current_row][current_col] = result  # 최댓값 기록
    return result


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    dp = [[-1] * N for _ in range(2)]  # 해당 스티커를 뗀 이후 얻을 수 있는 최고점수 기록
    sticker(0, 0)  # 위 스티커부터 탐색
    sticker(1, 0)  # 아래 스티커부터 탐색
    print(max(dp[0][0], dp[1][0]))