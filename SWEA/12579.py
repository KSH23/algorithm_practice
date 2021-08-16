# 12579. 앞글자따기


def first_letter(string):
    result = chr(ord(string[0]) -32)

    for i in range(1, len(string)):
        if string[i-1] == ' ':
            result += chr(ord(string[i]) -32)

    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    my_string = input()
    print('#{} {}'.format(tc, first_letter(my_string)))