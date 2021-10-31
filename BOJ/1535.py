# 1535. 안녕


import sys


def greet(person, life, joy):
    if life <= 0:  # 죽은 경우
        return 0

    if person == N:  # 마지막 사람까지 탐색한 경우
        return joy

    # person과 인사를 한 경우
    max_joy = greet(person + 1, life - lives[person], joy + joys[person])

    # person과 인사를 하지 않은 경우
    max_joy = max(max_joy, greet(person + 1, life, joy))

    return max_joy


N = int(sys.stdin.readline())
lives = list(map(int, sys.stdin.readline().split()))
joys = list(map(int, sys.stdin.readline().split()))
print(greet(0, 100, 0))