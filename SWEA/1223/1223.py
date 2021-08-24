# 1223. 계산기2


def postfix(equ):
    isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    ans = []
    for token in equation:
        if token == ')':
            while stack[-1] != '(':
                temp = stack.pop()
                ans.append(temp)
            stack.pop()
            continue

        if token not in icp:
            ans.append(token)
            continue

        if token == '(':
            stack.append(token)
            continue

        if len(stack) == 0 or icp[token] > isp[stack[-1]]:
            stack.append(token)

        else:
            while len(stack) > 0 and icp[token] <= isp[stack[-1]]:
                temp = stack.pop()
                ans.append(temp)
            stack.append(token)

    while len(stack) > 0:
        temp = stack.pop()
        ans.append(temp)

    return ans


def calculation(equ):
    stack = []

    for token in equation:
        if '0' <= token <= '9':
            stack.append(token)

        elif token == '/':
            if len(stack) < 2:
                return
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if num2 == 0:
                return
            stack.append(str(num1 // num2))

        elif token == '*':
            if len(stack) < 2:
                return
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            stack.append(str(num1 * num2))

        elif token == '-':
            if len(stack) < 2:
                return
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            stack.append(str(num1 - num2))

        elif token == '+':
            if len(stack) < 2:
                return
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            stack.append(str(num1 + num2))

    return stack[0]


for tc in range(1, 11):
    N = int(input())
    equation = input()
    print(postfix(equation))
    equation = ''.join(postfix(equation))
    # print(equation)
    equation = calculation(equation)
    print('#{} {}'.format(tc, equation))
