# 43238. 입국심사


def solution(n, times):
    left = 1  # 1분
    right = n * min(times)  # 모든 사람이 심라는 받는데 걸리는 최대 시간

    # 특정 시간 X분까지 심사할 수 있는 사람의 수는 각 심사관이 심사할 수 있는 시간을
    # X분에 대하여 나눈 몫의 합이므로 이분탐색을 통해 몫의 합이 n에 도달하도록 탐색
    while left < right:
        mid = (left + right) // 2  # 중간 시간

        cnt = sum(mid // time for time in times)  # 심사할 수 있는 사람의 수

        if n <= cnt:
            right = mid
        else:
            left = mid + 1

    return left
