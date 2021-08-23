# 12543. 부분집합의 합2


def dfs(now, sum, cnt):
    global ans

    if sum == K and cnt == N:
        ans += 1
        return
    if now >= 21:
        return

    if cnt < N and sum + now <= K:
        path[now] = 1
        dfs(now + 1, sum + now, cnt + 1)

    path[now] = 0
    dfs(now + 1, sum, cnt)

    path[now] = -1

    return


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    path = [-1] * 21
    ans = 0
    dfs(1, 0, 0)
    print('#{} {}'.format(tc, ans))
