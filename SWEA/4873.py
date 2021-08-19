# 4873. 반복문자 지우기


def str_del(string):
    stack = [string[0]]
    for letter in string[1:]:
        if len(stack) > 0 and letter == stack[-1]:
            stack.pop()
        else:
            stack += [letter]

    return len(stack)


T = int(input())
for tc in range(1, T+1):
    my_string = input()
    print('#{} {}'.format(tc, str_del(my_string)))