# 5099. 피자 굽기


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    q = []

    for idx, cheese in enumerate(C):
        C[idx] = [idx, cheese]

    # print(C)

    for _ in range(N):
        q.append(C.pop(0))

    while True:
        q[0][1] //= 2
        if q[0][1] <= 0:
            q.pop(0)
            if len(q) == 1:
                break
            if len(C) > 0:
                q.append(C.pop(0))

        q.append(q.pop(0))

    print('#{} {}'.format(tc, q[0][0] + 1))

