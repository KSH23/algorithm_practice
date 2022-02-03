# 12973. 짝지어 제거하기


def solution(s):
    stack = []

    for letter in s:
        if not stack:  # 스택이 빈 경우
            stack.append(letter)
            continue

        # 같은 문자를 발견한 경우 스택에서 제거 후 추가 안 함
        if letter == stack[-1]:
            stack.pop()

        # 다른 문자를 발견한 경우 스택에 추가
        else:
            stack.append(letter)

    if stack:
        return 1
    else:
        return 0