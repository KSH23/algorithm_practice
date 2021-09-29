# 1240. 단순 2진 암호코드


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    code_map = [input() for _ in range(N)]

    code_dict = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }

    # 우측하단부터 시작해 처음 등장하는 1 검사
    switch = 0
    for i in range(N - 1, -1, -1):
        if switch:
            break
        for j in range(M - 1, -1, -1):
            de=1

            if code_map[i][j] == '1':
                code_line = code_map[i][j-55:j + 1]
                switch = 1
                break

    decimal_code = []
    for i in range(0, 50, 7):
        decimal_code += [code_dict[code_line[i:i+7]]]

    final_num = 0
    for i in range(8):
        if i % 2 == 0:
            final_num += decimal_code[i] * 3
        else:
            final_num += decimal_code[i]

    if final_num % 10:
        ans = 0
    else:
        ans = sum(decimal_code)

    print(f'#{tc} {ans}')