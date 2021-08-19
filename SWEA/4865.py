# 4865. 글자수


def letter_num(n, m):
    cnt = [0] * (len(n))
    for i in range(len(n)):
        for char in m:
            if n[i] == char:
                cnt[i] += 1

    ans = cnt[0]
    for i in range(len(cnt)):
        if cnt[i] > ans:
            ans = cnt[i]

    return ans


T = int(input())
for tc in range(1, T+1):
    N = input()
    M = input()
    print('#{} {}'.format(tc, letter_num(N, M)))