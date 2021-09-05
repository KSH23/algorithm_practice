# 5174. subtree


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    node_list = list(map(int, input().split()))

    tree = [[] for _ in range(E+2)]

    for i in range(E):
        tree[node_list[2 * i]] += [node_list[2 * i + 1]]

    Q = [tree[N]]
    cnt = 1
    while len(Q) > 0:
        now = Q.pop(0)

        for node in now:
            Q += [tree[node]]
            cnt += 1

    print(f'#{tc} {cnt}')