# 12585. 문자열 비교


def compare(n, m):
    for i in range(len(m) - len(n) + 1):
        switch = 1
        if m[i] == n[0]:
            for j in range(len(n)):
                if m[i+j] != n[j]:
                    switch = 0
                    break
            if switch == 1:
                return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N = input()
    M = input()
    print('#{} {}'.format(tc, compare(N, M)))