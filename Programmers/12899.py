# 12899. 124 나라의 숫자


def solution(n):
    answer = ''

    # 3 제곱 수의 나머지와 몫을 이용할 예정이므로
    # 계산의 편의를 위해 n에서 1을 빼어 0부터 수를 세도록 함
    n -= 1

    # (n - 1)이 포함하고 있는 3 제곱 수의 개수 == 124 숫자의 자리 개수
    power_cnt = 1
    while 3 ** power_cnt <= n:
        n -= 3 ** power_cnt
        power_cnt += 1

    # 숫자를 3의 제곱 수로 나눌 때 그 나머지(인덱스)가 가르키는 124 숫자 규칙
    rule = ['1', '2', '4']

    while power_cnt:
        # 좌측 자리의 숫자부터 채워넣음
        # 현재 자리의 숫자는 (n // 3 ** (power_cnt - 1))가 포함된 개수
        answer += rule[n // 3 ** (power_cnt - 1)]

        # 다음 탐색할 자리수 감소
        n %= 3 ** (power_cnt - 1)
        power_cnt -= 1

    return answer