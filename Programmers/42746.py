# 42746. 가장 큰 수


def solution(numbers):
    # 모든 숫자가 최소한 4자리 수를 갖도록 만든 뒤 이를 사전 역순으로 정렬
    str_numbers = sorted(list(map(str, numbers)), reverse=True, key=lambda x: x * 4)

    # [0, 0, 0]과 같은 numbers가 주어진 경우 답이 000으로 나오지 않도록
    # 정수로 만든 뒤 다시 문자열로 변환
    answer = str(int(''.join(str_numbers)))

    return answer
