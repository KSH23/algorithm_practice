# 1221. GNS


def num_code(n, code):
    code_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    code_cnt = [0] * 10

    # 각 문자를 다 숫자로 바꿈
    for i in range(n):
        for j in range(10):
            if code_list[j] == code[i]:
                code_cnt[j] += 1

    result = ''
    for i in range(10):
        for j in range(code_cnt[i]):
            result += code_list[i] + ' '
            
    return result


T = int(input())

for tc in range(1, T + 1):
    N = int(input().split()[1])
    my_code = list(input().split())

    print('#{}\n{}'.format(tc, num_code(N, my_code)))