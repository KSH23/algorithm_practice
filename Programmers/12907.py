# 12907. 거스름돈


def solution(n, money):
    # change_cnt[index]: index 원을 만들 수 있는 경우의 수
    change_cnt = [0] * (n + 1)
    change_cnt[0] = 1  # 계산의 편의를 위해 1로 설정

    # 보유하고 있는 각 돈의 종류에 대해 경우의 수를 증가시킴
    for m in money:
        for index in range(1, n + 1):
            if 0 <= index - m:
                change_cnt[index] += change_cnt[index - m]

    return change_cnt[-1] % 1000000007
