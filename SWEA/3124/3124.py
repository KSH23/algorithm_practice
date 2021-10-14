# 3124. 최소 스패닝 트리(Kruskal's algorithm)


def find(x):  # 조상 찾기
    if parents[x] == x:
        return x

    p_x = find(parents[x])
    parents[x] = p_x  # 조상 갱신
    return p_x


def union(x, y):  # 조상 합치기
    p_x = find(x)
    p_y = find(y)
    parents[p_x] = p_y


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    parents = list(range(V + 1))  # 각 노드의 조상 저장
    edges = []

    for _ in range(E):
        A, B, weight = map(int, input().split())
        edges.append((weight, A, B))

    edges.sort()  # weight을 기준으로 정렬
    total_weight = 0
    for edge in edges:
        w, node1, node2 = edge[0], edge[1], edge[2]
        if find(node1) == find(node2):  # 조상이 같으면 무시
            continue
        total_weight += w
        union(node1, node2)  # 조상 합치기

    print(f'#{tc} {total_weight}')