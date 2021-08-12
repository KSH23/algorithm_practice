# 4839. 이진탐색


def binary_search(p, target):
    cnt = 0
    l = 1
    r = p

    while l < r:
        c = int((l + r) / 2)
        cnt += 1
        if c == target:
            return cnt
        elif target < c:
            r = c
        else:
            l = c

    return cnt


T = int(input())
for tc in range(1, 1+T):
    P, A, B = map(int, input().split())
    a = binary_search(P, A)
    b = binary_search(P, B)
    if a > b:
        winner = 'B'
    elif a < b:
        winner = 'A'
    else:
        winner = 0
    print('#{} {}'.format(tc, winner))