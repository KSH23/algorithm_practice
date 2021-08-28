# 12728. 이진 트리 전위 순회


def preorder_traverse(t):
    # 이 코드에서는 if문으로 tree[t]가 있는지 먼저 검사하면 안됨
    # 예를들어 t == 3일 때 tree[2*t] == 5,
    # 하지만 tree[5] == 0 이라서 그냥 넘어가버림

    ans.append(t)
    if tree[2*t] != 0:
        preorder_traverse(tree[2*t])
    if tree[2*t + 1] != 0:
        preorder_traverse(tree[2*t+1])


T = int(input())
for tc in range(1, T+1):
    V = int(input())
    tree = [0] * ((V + 1) * 2)
    tree[1] = 1
    for i in range(V - 1):
        p, c = map(int, input().split())
        if tree[p * 2] == 0:
            tree[p * 2] = c
        elif tree[p * 2] > c:
            tree[p * 2 + 1] = tree[p * 2]
            tree[p * 2] = c
        else:
            tree[p * 2 + 1] = c

    # print(tree)
    ans = []
    preorder_traverse(1)
    # print(ans)
    print('#{} {}'.format(tc, ' '.join(map(str, ans))))
