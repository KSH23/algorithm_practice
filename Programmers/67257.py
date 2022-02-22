# 67257. [카카오 인턴] 수식 최대화


import re


def calc(expression, priority):
    ret = []  # expression에서 priority 연산만을 진행한 결과 저장
    idx = 0
    while idx < len(expression):
        # 우선순위 연산자를 만난 경우 연산을 진행한 뒤 결과 리스트에 추가
        if expression[idx] == priority:
            pre_num = ret.pop()
            if expression[idx] == '*':
                ret.append(pre_num * (expression[idx + 1]))
            elif expression[idx] == '+':
                ret.append(pre_num + (expression[idx + 1]))
            else:
                ret.append(pre_num - (expression[idx + 1]))
            idx += 1  # 우선순위 연산자 뒤의 숫자는 탐색할 필요 없음

        # 우선순위에 해당하지 않는 연산자 또는 숫자는 리스트에 추가
        else:
            ret.append(expression[idx])

        idx += 1

    return ret


def solution(expression):
    answer = 0

    # 수식을 연산자와 숫자로 구분한 뒤 숫자는 정수로 변환
    expression = re.split('(\W)', expression)
    expression = [int(e) if e.isnumeric() else e for e in expression]

    # 연산자의 우선순위를 선정하여 매 연산자마다 계산을 하고 그 결과를 기록
    for first_priority in ['*', '-', '+']:
        first_expression = calc(expression, first_priority)
        for second_priority in ['*', '-', '+']:
            if first_priority == second_priority:
                continue
            second_expression = calc(first_expression, second_priority)
            for third_priority in ['*', '-', '+']:
                if second_priority == third_priority or first_priority == third_priority:
                    continue
                third_expression = calc(second_expression, third_priority)

                # 마지막 결과를 이용해 답을 갱신
                answer = max(answer, abs(third_expression[0]))

    return answer