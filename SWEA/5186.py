# 5186. 이진수2


def make_binary(num):
    binary_rtn = ''

    while num > 0:
        if len(binary_rtn) == 12:
            binary_rtn = 'overflow'
            break

        num *= 2

        if num >= 1:
            binary_rtn += '1'
            num -= 1
        else:
            binary_rtn += '0'

    return binary_rtn


T = int(input())
for tc in range(1, T+1):
    number = float(input())
    print(f'#{tc} {make_binary(number)}')