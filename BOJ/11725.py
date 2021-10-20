# 11725. 트리의 부모 찾기


import sys
from collections import deque


def make_tree(root):
    q = deque()
    q.append(root)  # 출발 노드 추가

    while q:
        cur_node = q.popleft()

        for node in tree[cur_node]:
            if node == 0:
                continue
            if parent[node]:
                continue
            parent[node] = cur_node
            q.append(node)


N = int(input())
tree = [[0] for _ in range(N + 1)]  # 연결 관계 저장
for _ in range(N - 1):
    node1, node2 = map(int, sys.stdin.readline().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

parent = [0] * (N + 1)
parent[1] = 1  # 루트의 부모를 루트로 설정

make_tree(1)
for idx in range(2, N + 1):
    print(parent[idx])