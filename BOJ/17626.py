# 17626. Four Squares


def dfs(num, cnt):
    if 4 <= cnt:  # 개수 최댓값이 4이므로 4 이상은 볼 필요 없음
        return 4

    if num == 0:  # 해를 구한 경우
        return cnt

    if dp[num]:  # 이미 구한 경우
        return dp[num]

    start_square = int(num ** 0.5)  # 현재 숫자의 제곱근
    last_square = int(start_square ** 0.5)  # 현재 숫자의 네제곱근

    result = 4
    for square in range(start_square, last_square - 1, -1):
        result = min(result, dfs(num - square ** 2, cnt + 1))

    dp[num] = result
    return result


N = int(input())
dp = [0] * (N + 1)  # 각 숫자의 해가되는 제곱수 개수 저장
print(dfs(N, 0))