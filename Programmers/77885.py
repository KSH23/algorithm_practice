# 77885. 2개 이하로 다른 비트


def solution(numbers):
    answer = []

    for number in numbers:
        number = int(number)

        i = 0
        while number & (1 << i):  # 0 비트를 처음 만나는 지점 탐색
            i += 1

        number ^= (1 << i)  # 처음 만나는 0 비트를 1로 토글

        # 만약 우측에 비트가 존재하는 경우 우측의 1 비트를 0으로 토글
        if i:
            number ^= (1 << (i - 1))

        answer.append(number)
    return answer
