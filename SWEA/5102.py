# 5102. 노드의 거리


from collections import deque


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    MAP = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        node1, node2 = map(int, input().split())
        MAP[node1][node2] = 1
        MAP[node2][node1] = 1

    S, G = map(int, input().split())

    Q = deque()
    Q.append(S)

    visited = [0] * (V+1)
    visited[S] = 1

    now = 0

    while now < len(Q):
        curr_node = Q[now]
        for i in range(1, V + 1):
            if MAP[curr_node][i] == 1 and visited[i] == 0:
                Q.append(i)
                visited[i] = visited[curr_node] + 1

        now += 1

    # print(visited)
    ans = visited[G] - 1
    if ans < 0:
        ans = 0
    print('#{} {}'.format(tc, ans))