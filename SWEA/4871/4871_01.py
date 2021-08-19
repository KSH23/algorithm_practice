# 4871. 그래프 경로


def dfs(now, g, v):
    global visited

    if now == g:
        return 1

    result = 0
    for i in range(1, v+1):
        if result == 1:
            break

        if node[now][i] == 1 and visited[i] == 0:
            next = i
            visited[i] = 1
            result = dfs(next, g, v)

    if result == 1:
        return result

    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        node[s][e] += 1    # 방향성 그래프

    result = 0

    S, G = map(int, input().split())
    visited = [0] * (V+1)
    visited[S] = 1

    ans = dfs(S, G, V)

    print('#{} {}'.format(tc, ans))
