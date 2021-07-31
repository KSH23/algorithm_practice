"""
1216: 회문2
"""

import sys
sys.stdin = open('1216_input.txt')


def is_palindrome(word):    # 회문 확인 함수
    for i in range(len(word) // 2):
        if word[i] != word[-1-i]:
            return False
    return True


def max_palindrome(palindrome):
    for n in range(100, -1, -1):
        # h는 가로줄, v는 세로줄
        for h in range(100):
            for v in range(100 - n + 1):
                temp_h_word = ''    # 매 번 확인할 str 변수
                temp_v_word = ''
                for i in range(n):
                    temp_h_word += palindrome[h][v+i]
                    # 가로줄과 세로줄을 반대로 해서 세로 글자를 만듦
                    temp_v_word += palindrome[v+i][h]
                
                if is_palindrome(temp_h_word):
                    return n
                if is_palindrome(temp_v_word):
                    return n


T = 10

for tc in range(1, T+1):
    no = int(input())

    my_palindrome = []
    for i in range(100):
        my_palindrome.append(list(input()))

    print(f'#{tc} {max_palindrome(my_palindrome)}')