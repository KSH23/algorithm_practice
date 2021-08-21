# 1219. 길찾기


def dfs(now):
    global visited

    for i in range(100):
        if route[now][i] == 1 and visited[i] == 0:
            visited[i] = 1
            next = i
            dfs(next)


T = 10
for tc in range(1, T+1):
    t, E = list(map(int, input().split()))
    route = [[0] * 100 for _ in range(100)]
    line = list(map(int, input().split()))

    for i in range(E):
        route[line[2 * i]][line[2 * i + 1]] = 1

    visited = [0] * 100

    dfs(0)

    print('#{} {}'.format(tc, visited[99]))