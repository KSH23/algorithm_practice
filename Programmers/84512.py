# 84512. 모음 사전


def solution(word):
    answer = 0

    # 각 알파벳이 갖는 순서 기록
    order = {"A": 0, "E": 1, "I": 2, "O": 3, "U": 4}

    # 각 자릿수에 따라 추가되어야 하는 수
    # [5^4 + 5^3 + 5^2 + 5, 5^3 + 5^2 + 5, 5^2 + 5, 5, 0]
    multiply_five = [sum(5 ** i for i in range(1, j + 1)) for j in range(4, -1, -1)]
    
    # 각 자릿수에 따라 추가되어야 하는 수에 1을 더하고 이를 알파벳 순서만큼 추가로 곱함
    for index, letter in enumerate(word):
        answer += (multiply_five[index] + 1) * order[letter] + 1

    return answer
