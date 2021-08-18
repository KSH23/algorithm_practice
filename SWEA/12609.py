# 12609. 스택 연습


def add(stack, num):
    stack.append(num)
    return


def c(stack):
    return len(stack)


def o(stack):
    if len(stack) == 0:
        return 'empty'
    else:
        return stack.pop()


T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc))
    N = int(input())
    a = []
    for i in range(N):
        order = list(input())

        if order[0] == 'i':
            add(a, int(order[2]))

        elif order[0] == 'c':
            print(c(a))
        else:
            print(o(a))

