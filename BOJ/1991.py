# 1991. 트리 순회


def preorder(parent='A'):
    if parent == '.':
        return

    left = tree_dict[parent][0]
    right = tree_dict[parent][1]

    print(parent, end='')
    preorder(left)
    preorder(right)


def inorder(parent='A'):
    if parent == '.':
        return

    left = tree_dict[parent][0]
    right = tree_dict[parent][1]

    inorder(left)
    print(parent, end='')
    inorder(right)


def postorder(parent='A'):
    if parent == '.':
        return

    left = tree_dict[parent][0]
    right = tree_dict[parent][1]

    postorder(left)
    postorder(right)
    print(parent, end='')


N = int(input())
tree_dict = {}
for _ in range(N):
    temp = input().split()
    tree_dict[temp[0]] = [temp[1], temp[2]]

preorder()
print()
inorder()
print()
postorder()
print()