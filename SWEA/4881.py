# 4881. 배열 최소 합


def dfs(r):
    global cnt, ans

    if r == N:
        if ans > cnt:
            ans = cnt
        return

    if cnt > ans:
        return

    for i in range(N):
        if col[i] == 0:
            cnt += MAP[r][i]
            col[i] = 1
            dfs(r + 1)
            col[i] = 0
            cnt -= MAP[r][i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    col = [0] * N
    cnt = 0
    ans = 5000
    dfs(0)
    print('#{} {}'.format(tc, ans))
