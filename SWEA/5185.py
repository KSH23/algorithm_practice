# 5185. 이진수


def make_binary4(num):
    binary_rtn = ''
    while num > 0:
        if num % 2:
            binary_rtn = '1' + binary_rtn
        else:
            binary_rtn = '0' + binary_rtn
        num //= 2

    binary_rtn = '0' * (4 - len(binary_rtn)) + binary_rtn

    return binary_rtn


T = int(input())
for tc in range(1, T+1):
    N, hexadecimal = input().split()
    N = int(N)
    hexadecimal_dict = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    binary_str = ''
    print(f'#{tc} ', end='')
    for h in hexadecimal:
        if h.isdigit():
            h = int(h)
        else:
            h = hexadecimal_dict[h]
        print(make_binary4(h), end='')
    print()