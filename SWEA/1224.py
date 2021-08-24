# 1224. 계산기3


def postfix(equ):
    stack = []
    result = ''
    for token in equ:
        if '0' <= token <= '9':
            result += token
        elif token == '+':
            while len(stack) > 0 and stack[-1] != '(':
                result += stack.pop()
            stack.append(token)
        elif token == '*':
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()

    while len(stack) > 0:
        result += stack.pop()

    return result


def calculation(equ):
    stack = []
    for token in equ:
        if '0' <= token <= '9':
            stack.append(token)
        elif token == '+':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a + b)
        elif token == '*':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a * b)

    return stack[0]



for tc in range(1, 11):
    N = int(input())
    equation = input()
    equation = postfix(equation)
    # print(equation)
    # print(equation)
    equation = calculation(equation)
    print('#{} {}'.format(tc, equation))
