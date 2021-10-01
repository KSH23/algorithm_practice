# 10726. 이진수 표현


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    temp = M & ((1 << N) - 1)
    if temp == 2 ** N - 1:
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')