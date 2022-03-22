# 12909. 올바른 괄호


def solution(s):
    stack = []
    for letter in s:
        if letter == "(":  # 열리는 괄호는 무조건 스택에 추가
            stack.append(letter)
        else:  # 현재 괄호가 닫히는 괄호인 경우
            if stack and stack.pop() == "(":  # 올바른 괄호를 맞출 수 있는 경우
                continue
            else:  # 스택에 괄호가 없거나 올바른 괄호를 맞출 수 없는 경우
                return False
            
    if stack:  # 스택에 맞춰지지 않은 괄호가 남아있는 경우
        return False
    return True