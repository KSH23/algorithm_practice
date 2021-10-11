# 15681. 트리와 쿼리


import sys


sys.setrecursionlimit(1000000)


def counting_nodes(node, parent):
    ret = 1  # 현재 정점도 개수에 포함
    for idx in list(graph[node]):
        if idx == parent:  # 부모는 제외
            continue
        ret += counting_nodes(idx, node)

    node_cnt[node] = ret  # 정점의 수 갱신
    return ret


N, R, Q = map(int, input().split())
graph = [set() for _ in range(N + 1)]
for _ in range(N - 1):
    U, V = map(int, sys.stdin.readline().split())
    graph[U].add(V)  # 정점과 정점간 연결관계 표시
    graph[V].add(U)  # 정점과 정점간 연결관계 표시

node_cnt = [0] * (N + 1)  # 각 인덱스를 루트로 갖는 서브트리의 정점의 수
counting_nodes(R, -1)

for _ in range(Q):
    q = int(sys.stdin.readline())
    print(node_cnt[q])