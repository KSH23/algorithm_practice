# 4866. 괄호검사


def bracket(string):
    stack = []
    for letter in string:
        if letter == '(' or letter == '{':
            stack += [letter]
        elif letter == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return 0
            else:
                stack.pop()
        elif letter == '}':
            if len(stack) == 0 or stack[-1] != '{':
                return 0
            else:
                stack.pop()

    if len(stack) == 0:
        return 1
    else:
        return 0


T = int(input())

for tc in range(1, T+1):
    code = input()
    print('#{} {}'.format(tc, bracket(code)))
