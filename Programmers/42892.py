# 42892. 길 찾기 게임


import sys

sys.setrecursionlimit(10 ** 5)


class Node:
    def __init__(self, index, x):
        self.index = index
        # 부모와 자식 관계가 정렬되어 있으므로 y 값은 고려할 필요 없음
        self.x = x
        self.left, self.right = None, None


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def insert(self, index, x):
        current_node = self.root

        # 노드를 정렬해 자식 노드가 부모 노드보다 먼저 나올 일 없기 때문에
        # 현재 노드의 자식을 탐색하며 자식이 없는 자리에 노드를 추가
        while True:
            if x < current_node.x:  # 왼쪽 서브 트리에 들어가는 경우
                if current_node.left:
                    current_node = current_node.left
                    continue
                current_node.left = Node(index, x)  # 자식 추가
                break
            else:  # 오른쪽 서브 트리에 들어가는 경우
                if current_node.right:
                    current_node = current_node.right
                    continue
                current_node.right = Node(index, x)  # 자식 추가
                break


def pre_order(node):  # 전위 순회
    ret = [node.index]
    if node.left:
        ret += pre_order(node.left)
    if node.right:
        ret += pre_order(node.right)
    return ret


def post_order(node):  # 후위 순회
    ret = []
    if node.left:
        ret += post_order(node.left)
    if node.right:
        ret += post_order(node.right)
    ret.append(node.index)
    return ret


def solution(node_info):
    # 인덱스를 포함하여 노드 정보를 갱신하고 이를 y 좌표 내림차순, x 좌표 오롬차순으로 정렬
    nodes = sorted([item + [index + 1] for index, item in enumerate(node_info)], key=lambda item: (-item[1], item[0]))

    root = Node(nodes[0][2], nodes[0][0])
    tree = BinaryTree(root)

    for x, y, index in nodes[1:]:
        tree.insert(index, x)  # 트리 생성

    answer = [pre_order(root), post_order(root)]

    return answer
