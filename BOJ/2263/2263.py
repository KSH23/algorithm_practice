# 2263. 트리의 순회


import sys

sys.setrecursionlimit(200000)


def preorder(ps_idx, pe_idx, is_idx, ie_idx):
    """
    :param ps_idx: postorder start index
    :param pe_idx: postorder end index
    :param is_idx: inorder start index
    :param ie_idx: inorder end index
    """
    print(postorder[pe_idx], end=' ')

    if ps_idx == pe_idx:  # 리프노드 도달
        return

    # 현재 서브 트리의 루트는 postorder[pe_idx]
    # 서브 트리의 루트가 inorder 리스트에서 갖는 인덱스 값을 찾음
    inorder_root_idx = inorder_index_dict[postorder[pe_idx]]

    # inorder 리스트에서 현재 서브 트리의 좌측 자식 노드 개수와 우측 자식 노드 개수
    left_range = inorder_root_idx - is_idx - 1
    right_range = ie_idx - inorder_root_idx - 1

    # 다음 서브 트리에 해당하는 postorder 리스트와 inorder 리스트의 범위를 넘김
    if 0 <= left_range:
        preorder(ps_idx, ps_idx + left_range, is_idx, inorder_root_idx - 1)
    if 0 <= right_range:
        preorder(pe_idx - 1 - right_range, pe_idx - 1, inorder_root_idx + 1, ie_idx)


N = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))

inorder_index_dict = {}  # 노드 번호와 그에 해당하는 인덱스 저장
for index, value in enumerate(inorder):
    inorder_index_dict[value] = index

postorder = list(map(int, sys.stdin.readline().split()))
preorder(0, N - 1, 0, N - 1)