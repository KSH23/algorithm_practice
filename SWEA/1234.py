# 1234. 비밀번호


def pwd(string):
    stack = string[0]
    for letter in string[1:]:
        if len(stack) > 0 and letter == stack[-1]:
            stack = stack[:-1]
        else:
            stack += letter

    return stack


T = 10
for tc in range(1, T+1):
    N, my_string = input().split()
    print('#{} {}'.format(tc, pwd(my_string)))