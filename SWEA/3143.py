# 3143. 가장 빠른 문자열 타이핑


def typing(a, b):
    cnt = 0
    i = 0

    while i < len(a):
        if i <= len(a) - len(b) and a[i] == b[0]:
            switch = 0
            for j in range(len(b)):
                if a[i + j] != b[j]:
                    switch = 0
                else:
                    switch += 1
            if switch == len(b):
                cnt += 1
                i += len(b)
            else:
                cnt += 1
                i += 1
        else:
            i += 1
            cnt += 1

    return cnt


T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    print('#{} {}'.format(tc, typing(A, B)))