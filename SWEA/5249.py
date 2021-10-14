# 5249. 최소 신장 트리


def find(x):
    if parents[x] == x:
        return x

    p_x = find(parents[x])
    parents[x] = p_x
    return p_x


def union(x, y):
    p_x = find(x)
    p_y = find(y)
    parents[p_x] = p_y


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    parents = [0] + list(range(1, V + 1))
    edges = []

    for _ in range(E):
        n1, n2, weight = map(int, input().split())
        edges.append((weight, n1, n2))

    edges.sort()
    total_weight = 0
    for edge in edges:
        w, node1, node2 = edge[0], edge[1], edge[2]
        if find(node1) == find(node2):
            continue
        total_weight += w
        union(node1, node2)

    print(f'#{tc} {total_weight}')