# 17687. [3차] n진수 게임


def convert_integer(number, base):
    """
    :param number: 변환하고자 하는 정수
    :param base: 변환하고자 하는 진수
    :return: base 진수로 변환한 number의 string
    """
    ret = ""
    while number:
        if 10 <= number % base:  # A ~ F로 반환해야 하는 경우
            ret = chr(number % base + 55) + ret
        else:
            ret = str(number % base) + ret
        number //= base
    return ret


def solution(n, t, m, p):
    answer = ""
    current_game = "0"  # 게임 기록
    next_number = 1  # 다음에 말해야 할 숫자

    for repeat in range(t):
        turn = repeat * m + p - 1  # 튜브의 순서

        # 튜브가 말할 숫자가 존재할 때 까지 게임 진행
        while len(current_game) <= turn:
            current_game += convert_integer(next_number, n)
            next_number += 1

        answer += current_game[turn]  # 튜브가 말해야 할 숫자

    return answer
