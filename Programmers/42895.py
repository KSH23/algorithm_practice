# 42895. N으로 표현


def solution(N, number):
    if N == number:  # 예외 경우
        return 1

    # 인덱스: N의 사용 횟수, 값: 만들 수 있는 숫자들의 집합
    dp = [set(), {N}]

    for index in range(2, 9):  # N의 사용 횟수는 8회로 제한
        temp = {int(str(N) * index)}  # N을 index개만큼 이어붙인 숫자

        for sub_index in range(1, index):
            for i in dp[sub_index]:  # dp의 1, 2, 3, ... 인덱스에 해당하는 값
                for j in dp[index - sub_index]:  # dp의 -1, -2, -3, ... 인덱스에 해당하는 값
                    # 가능한 사칙연산을 모두 적용
                    temp.add(i + j)
                    temp.add(i - j)
                    if j:
                        temp.add(i // j)
                    temp.add(i * j)

        if number in temp:  # number을 만난 경우
            return index
        dp += [temp]

    return -1
