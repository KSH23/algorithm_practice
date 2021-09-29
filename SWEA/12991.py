# 12991. 이진수의 3의 배수


def calc_c(a, b):
    up = down = 1
    for cnt in range(b):
        up *= a
        a = a - 1
    for cnt in range(b):
        down *= b
        b = b - 1

    return up // down


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    ans = 0
    for i in range(K + 1):
        if (2 * i - K) % 3 == 0:
            if N % 2:
                ans += calc_c(N - (N // 2 + 1), i) * calc_c(N // 2 + 1, K - i)
            else:
                ans += calc_c(N // 2, i) * calc_c(N // 2, K - i)

    print(f'#{tc} {ans}')