# 4871. 그래프 경로


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

    stack = [S]
    while len(stack) > 0:
        if stack[-1] == G:
            result = 1
            break

        cnt = 0
        for i in range(1, V+1):
            if node[stack[-1]][i] == 1 and visited[i] == 0:
                stack += [i]
                visited[i] = 1
                break
            else:
                cnt += 1
        if cnt == V:
            stack.pop()

    print('#{} {}'.format(tc, result))
