# 12945. 피보나치 수


def solution(n):
    # 피보나치 초기값 반환
    if n < 2:
        return n

    fibonacci = [0] * (n + 1)  # 피보나치 수 저장 리스트
    fibonacci[1] = 1

    # 피보나치 수 갱신
    for num in range(2, n + 1):
        fibonacci[num] = (fibonacci[num - 1] + fibonacci[num - 2]) % 1234567

    return fibonacci[n]