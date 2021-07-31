"""
1215: 회문1
"""

import sys
sys.stdin = open('1215_input.txt')


def is_palindrome(word):    # 회문 확인 함수
    for i in range(len(word) // 2):
        if word[i] != word[-1-i]:
            return False
    return True


def count_palindrome(n, palindrome):
    count = 0

    # h는 가로줄, v는 세로줄
    for h in range(8):
        for v in range(8 - n + 1):
            temp_h_word = ''    # 매 번 확인할 str 변수
            temp_v_word = ''
            for i in range(n):
                temp_h_word += palindrome[h][v+i]
                # 가로줄과 세로줄을 반대로 해서 세로 글자를 만듦
                temp_v_word += palindrome[v+i][h]
            
            if is_palindrome(temp_h_word):
                count += 1
            if is_palindrome(temp_v_word):
                count += 1

    return count


T = 10

for tc in range(1, T+1):
    N = int(input())

    my_palindrome = []
    for i in range(8):
        my_palindrome.append(list(input()))

    print(f'#{tc} {count_palindrome(N, my_palindrome)}')
