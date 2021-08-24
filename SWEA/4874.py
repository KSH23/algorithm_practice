# 4874. Forth


T = int(input())
for tc in range(1, T+1):
    equation = list(input().split())
    stack = []

    print('#{}'.format(tc), end=' ')

    for token in equation:
        if '0' <= token <= '9':
            stack.append(token)

        elif token == '.':
            if len(stack) != 1:
                print('error')
                break
            print(stack[0])

        elif token == '/':
            if len(stack) < 2:
                print('error')
                break
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if num2 == 0:
                print('error')
                break
            stack.append(str(num1 // num2))

        elif token == '*':
            if len(stack) < 2:
                print('error')
                break
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            stack.append(str(num1 * num2))

        elif token == '-':
            if len(stack) < 2:
                print('error')
                break
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            stack.append(str(num1 - num2))

        elif token == '+':
            if len(stack) < 2:
                print('error')
                break
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            stack.append(str(num1 + num2))