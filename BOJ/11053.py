# 11053. 가장 긴 증가하는 부분 수열


import sys


def find_longest(idx):
    if N < idx:  # 범위 밖
        return 0

    if -1 < memo[idx]:  # 이미 계산된 경우
        return memo[idx]

    longest_length = 1  # 최장 길이
    for next_idx in range(idx + 1, N + 1):
        if sequence[idx] < sequence[next_idx]:
            # 최장 길이 갱신
            longest_length = max(longest_length, find_longest(next_idx) + 1)

    memo[idx] = longest_length  # 최장 길이 저장
    return longest_length


N = int(sys.stdin.readline())

# 함수 내에서 0번 인덱스부터 for loop를 돌리기 위해 앞에 [0] 추가
sequence = [0] + list(map(int, sys.stdin.readline().split()))
memo = [-1] * (N + 1)  # 해당 인덱스에서 시작하는 가장 긴 증가하는 부분 수열 길이 저장
find_longest(0)
print(max(memo[1:]))