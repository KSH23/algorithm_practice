# 1242. 암호코드 스캔


import sys

sys.stdin = open('1242_input.txt')


def find_code():
    global code_set

    for r in range(N - 1, -1, -1):
        for c in range(M - 1, -1, -1):
            if code_map[r][c] != '0':
                code_set.add(code_map[r][:c + 1].rstrip('0'))
                break


def make_pretty_code(ugly_code):
    pretty_code = ''

    for letter in ugly_code:
        if letter == '0':
            pretty_code += '0000'
        elif '1' <= letter <= '9':
            for order in range(3, -1, -1):
                if (ord(letter) - ord('0')) & (1 << order):
                    pretty_code += '1'
                else:
                    pretty_code += '0'
        else:
            for order in range(3, -1, -1):
                if (ord(letter) - ord('A') + 10) & (1 << order):
                    pretty_code += '1'
                else:
                    pretty_code += '0'
    return pretty_code.rstrip('0')


def make_decimal_code(some_str, s):
    code_dict = {
        '0001101': '0',
        '0011001': '1',
        '0010011': '2',
        '0111101': '3',
        '0100011': '4',
        '0110001': '5',
        '0101111': '6',
        '0111011': '7',
        '0110111': '8',
        '0001011': '9'
    }
    some_str = some_str[::s]

    decimal_code = ''
    for idx in range(0, 56, 7):
        if some_str[idx:idx + 7] not in code_dict.keys():
            return ''
        decimal_code += code_dict[some_str[idx:idx + 7]]

    return decimal_code


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    code_map = [input() for _ in range(N)]
    code_set = set()
    find_code()
    final_code_set = set()
    for code in code_set:
        binary_code = '0' * 56 + make_pretty_code(code)
        size = 1
        while binary_code:
            last = len(binary_code)
            guess = binary_code[last - size * 56:]
            guess_result = make_decimal_code(guess, size)

            if not guess_result:
                size += 1
            else:
                final_code_set.add(guess_result)
                binary_code = binary_code[:last - size * 56]
                binary_code = binary_code.rstrip('0')
                size = 1

    ans = 0
    for final in final_code_set:
        result = 0
        temp_ans = 0
        for i in range(len(final)):
            if i % 2 == 0:
                result += int(final[i]) * 3
            else:
                result += int(final[i])
            temp_ans += int(final[i])

        if result % 10 == 0:
            ans += temp_ans

    print(f'#{tc} {ans}')