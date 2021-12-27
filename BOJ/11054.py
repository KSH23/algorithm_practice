# 11054. 가장 긴 바이토닉 부분 수열


import sys


def find_sequence(start_idx, d):
    """
    :param start_idx: 기준이 되는 시작 인덱스
    :param d: 방향. 0일땐 좌측으로, 1일땐 우측으로 탐색
    :return: start_idx에서 d방향으로 최장 감소하는 부분 수열의 길이
    """
    if -1 < dp[start_idx][d]:  # 이미 탐색한 경우
        return dp[start_idx][d]

    ret = 1
    # 좌측: range(start_idx - 1, -1, -1)
    # 우측: range(start_idx + 1, N, 1)
    for idx in range(start_idx + (2 * d) - 1, (N + 1) * d - 1, (2 * d) - 1):
        if num_list[idx] < num_list[start_idx]:
            ret = max(ret, find_sequence(idx, d) + 1)

    dp[start_idx][d] = ret
    return ret


N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

# 인덱스를 기준으로 좌측과 우측에 있는 감소하는 작은 수의 개수 기록
dp = [[-1, -1] for _ in range(N)]
dp[0][0] = dp[N - 1][1] = 1

for index in range(0, N):
    # index를 기준으로 좌측과 우측의 감소하는 작은 수를 탐색
    find_sequence(index, 0)
    find_sequence(index, 1)

# dp[index]의 합이 최대인 값을 고르고
# index는 중복되어 2번 포함되어 있으므로 1을 빼야 한다
print(max(sum(i) for i in dp) - 1)