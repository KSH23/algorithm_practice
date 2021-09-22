# 9019. DSLR


import sys
from collections import deque


T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    visited_number = [0] * 10000
    visited_number[A] = 1
    queue = deque()
    queue.append([A, ''])

    flag = 0
    while len(queue) > 0:
        now = queue.popleft()
        cur_num = now[0]
        cur_func = now[1]

        if flag:
            break

        for func in range(4):
            if func == 0:    # D의 경우
                new_num = (cur_num * 2) % 10000
                new_func = cur_func + 'D'
            elif func == 1:    # S의 경우
                new_num = cur_num - 1
                if new_num < 0:
                    new_num = 9999
                new_func = cur_func + 'S'
            elif func == 2:    # L의 경우
                new_num = cur_num * 10 % 10000 + cur_num * 10 // 10000
                new_func = cur_func + 'L'
            else:    # R의 경우
                new_num = cur_num // 10 + (cur_num % 10) * 1000
                new_func = cur_func + 'R'

            if visited_number[new_num] == 1:
                continue

            if new_num == B:
                print(new_func)
                flag = 1

            visited_number[new_num] = 1
            queue.append([new_num, new_func])