# 1232. 사칙연산


def inorder(now):
    if now > N:
        return 0
    if node[now] != '+' and node[now] != '-' and node[now] != '*' and node[now] != '/':
        return node[now]

    left = inorder(tree[now][0])
    right = inorder(tree[now][1])

    if node[now] == '+':
        return left + right
    elif node[now] == '-':
        return left - right
    elif node[now] == '*':
        return left * right
    else:
        return left / right


T = 10
for tc in range(1, T+1):
    N = int(input())
    node = [0] * (N + 1)
    tree = [0, 0] * (N + 1)
    for idx in range(N):
        temp = input().split()
        if len(temp) == 4:
            cur_node = int(temp[0])
            node[cur_node] = temp[1]
            tree[cur_node] = [int(temp[2]), int(temp[3])]
        else:
            cur_node = int(temp[0])
            node[cur_node] = int(temp[1])

    print(f'#{tc} {int(inorder(1))}')