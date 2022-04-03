# 92335. k진수에서 소수 개수 구하기


def change_base(number, base):
    """
    :param number: 진법을 변환하고자 하는 숫자
    :param base: 진수
    :return: base 진수로 변환된 number를 문자열로 반환
    """
    ret = ""
    while number:
        ret = str(number % base) + ret
        number //= base

    return ret


def is_prime(number):
    """
    :param number: 소수인지 판별하고자 하는 숫자
    :return: 소수 여부
    """
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    n = change_base(n, k)  # k진수로 변환

    left = 0  # 0이 아닌 숫자가 시작되는 인덱스 기록
    while left < len(n):
        while left < len(n) and n[left] == "0":
            left += 1

        right = left + 1  # 0을 만나게 되는 인덱스 기록
        while right < len(n) and n[right] != "0":
            right += 1

        # left부터 right까지의 숫자가 소수인지 판별
        if n[left: right] and is_prime(int(n[left: right])):
            answer += 1

        left = right  # left 인덱스 이동

    return answer
