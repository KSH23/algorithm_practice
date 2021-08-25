# 12649. N Castle


def dfs(i):
    global ans

    if i == N:
        ans += 1
        return

    for k in range(N):
        if col[k] == 1:
            continue

        col[k] = 1
        dfs(i + 1)
        col[k] = 0

    return


for tc in range(1, 11):
    N = int(input().rstrip())
    col = [0] * N
    ans = 0
    dfs(0)
    print('#{} {}'.format(tc, ans))