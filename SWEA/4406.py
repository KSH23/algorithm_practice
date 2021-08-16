# 4406. 모음이 보이지 않는 사람


def no_vowels(string):
    result = ''
    vowels = ['a', 'i', 'u', 'e', 'o']
    for letter in string:
        if letter in vowels:
            continue
        else:
            result += letter

    return result


T = int(input())
for tc in range(1, T+1):
    my_string = input()
    print('#{} {}'.format(tc, no_vowels(my_string)))