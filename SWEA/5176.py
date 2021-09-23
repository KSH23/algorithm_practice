# 5176. 이진탐색


def dfs(now):
    global num

    if now * 2 <= N:
        dfs(now * 2)
    tree[now] = num
    num += 1
    if now * 2 + 1 <= N:
        dfs(now * 2 + 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)
    num = 1
    dfs(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))