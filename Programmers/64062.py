# 64062. 징검다리 건너기


def solution(stones, k):
    left, right = 1, 200000000  # 밟힌 횟수 카운터

    while left <= right:
        mid = (left + right) // 2  # 지금까지 다리를 건넌 친구 수

        count = 0  # 건널 수 없는 연속된 돌의 개수
        for number in stones:
            if number - mid <= 0:  # 돌을 건널 수 없는 경우
                count += 1
                if k <= count:  # 가지치기
                    break
            else:
                count = 0  # 돌의 개수 초기화

        if k <= count:  # 너무 많이 밟은 경우
            right = mid - 1
        elif count < k:  # 너무 적게 밟은 경우
            left = mid + 1

    return left
