"""
1221: GNS
"""

import sys
sys.stdin = open('1221_input.txt')


def num_code(n, code):
    # 각 문자와 숫자가 key, val을 형성하는 딕셔너리 생성
    num_code_list = list(range(10))
    code_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    code_dict = dict(zip(code_list, num_code_list))
    
    # 각 문자를 다 숫자로 바꿈
    for i in range(n):
        for key, val in code_dict.items():
            if code[i] == key:
                code[i] = val
    
    # 숫자 리스트 정렬
    code.sort()

    # 각 숫자를 다 문자로 바꿈
    for i in range(n):
        for key, val in code_dict.items():
            if code[i] == val:
                code[i] = key


    return code


T = int(input())

for tc in range(1, T+1):
    N = int(input().split()[1])
    my_code = list(input().split())

    print(f'#{tc}\n {" ".join(num_code(N, my_code))}')