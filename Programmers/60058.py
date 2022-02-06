# 60058. 괄호 변환


def good_bracket(string):
    stack = []
    for letter in string:
        # 스택이 비어있는 경우
        if not stack:
            # 우측 괄호가 들어오면 올바른 괄호 문자열 아님
            if letter == ")":
                return False
            stack.append(letter)

        # 좌측 괄호는 스택에 추가
        elif letter == "(":
            stack.append(letter)

        # 스택에 괄호가 있는데 우측 괄호가 등장한 경우
        else:
            # 스택의 마지막 문자(좌측 괄호) 한 개 제거
            stack.pop()

    # 스택에 괄호가 남은 경우 올바른 괄호 문자열 아님
    if stack:
        return False

    return True


def solution(w):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if not w:
        return w

    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
    u, v = "", ""
    bracket_cnt_dict = {"(": 0, ")": 0}  # 괄호 개수 저장 딕셔너리
    for idx, letter in enumerate(w):
        bracket_cnt_dict[letter] += 1

        # 균형잡힌 괄호 문자열을 생성한 경우 해당 인덱스로 u와 v 문자열을 나눔
        if bracket_cnt_dict["("] == bracket_cnt_dict[")"]:
            u, v = w[0: idx + 1], w[idx + 1:]
            break

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    if good_bracket(u):
        # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
        return u + solution(v)

    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    else:
        #  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        #  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        #  4-3. ')'를 다시 붙입니다.
        #  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        #  4-5. 생성된 문자열을 반환합니다.
        return "(" + solution(v) + ")" + u[1: -1].replace("(", "a").replace(")", "(").replace("a", ")")