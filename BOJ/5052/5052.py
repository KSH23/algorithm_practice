# 5052. 전화번호 목록


import sys


def phone_book(num_list):
    num_list.sort()

    for i in range(len(num_list) - 1):
        if num_list[i] == num_list[i+1][0: len(num_list[i])]:
            return 'NO'

    return 'YES'


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    my_num_list = [sys.stdin.readline().rstrip() for _ in range(N)]

    print(phone_book(my_num_list))
