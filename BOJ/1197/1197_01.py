# 1197. 최소 스패닝 트리(Prim)


from sys import stdin


def prim():
    visited = [0] * (V + 1)
    weights = [0] + [1000001] * V  # 선택된 간선의 가중치 저장 리스트

    weights[1] = 0  # 1번 노드를 초기 노드로 설정

    for _ in range(V):
        # 최소 가중치의 간선을 가진 노드를 선택
        min_node = 0
        min_weight = 1000000
        for node in range(1, V + 1):
            if visited[node]:
                continue
            if weights[node] < min_weight:
                min_node = node
                min_weight = weights[node]

        visited[min_node] = 1  # 노드 확정

        # 확정된 노드에 연결된 노드와 가중치를 살피며 최솟값 갱신
        for next_node, w in edges[min_node]:
            if visited[next_node]:
                continue
            if weights[next_node] <= w:
                continue
            weights[next_node] = w

    return sum(weights)


V, E = map(int, input().split())
parents = list(range(V + 1))  # 각 정점의 조상 저장
edges = [[] for _ in range(V + 1)]
for _ in range(E):
    node1, node2, weight = list(map(int, stdin.readline().split()))
    edges[node1].append([node2, weight])
    edges[node2].append([node1, weight])

print(prim())