# 5178. 노드의 합


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 2)
    for leaf in range(M):
        node, value = map(int, input().split())
        tree[node] = value

    node_num = N
    while node_num > 0:
        if tree[node_num]:
            node_num -= 1
            continue
        tree[node_num] = tree[node_num * 2] + tree[node_num * 2 + 1]

    print(f'#{tc} {tree[L]}')