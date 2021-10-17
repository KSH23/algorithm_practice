# 1197. 최소 스패닝 트리(Kruskal)


from sys import stdin


def find(x):
    while parents[x] != x:
        x = parents[x]
    parents[x] = x
    return x


def union(x, y):
    parents[find(y)] = find(x)


V, E = map(int, input().split())
parents = list(range(V + 1))  # 각 정점의 조상 저장
edges = [list(map(int, stdin.readline().split())) for _ in range(E)]
edges.sort(key=lambda i: i[2])  # 가중치를 기준으로 정렬

total_weight = 0  # 최종 가중치
for edge in edges:
    node1, node2, weight = edge
    if find(node1) == find(node2):
        continue  # 만약 두 노드의 조상이 같다면 이후 계산 필요 없음
    total_weight += weight
    union(node1, node2)  # 두 노드를 합침

print(total_weight)