# 10804. 문자열의 거울상


# string[-1::-1] 하면 그냥 바로 뒤집어지기는 함
def mirror(string):
    result = ''
    for letter in string:
        if letter == 'b':
            result = 'd' + result
        elif letter == 'd':
            result = 'b' + result
        elif letter == 'p':
            result = 'q' + result
        else:
            result = 'p' + result

    return result


T = int(input())
for tc in range(1, T+1):
    my_string = input()
    print('#{} {}'.format(tc, mirror(my_string)))