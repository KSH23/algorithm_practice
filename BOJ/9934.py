# 9934. 완전 이진 트리


def inorder(now, depth):
    global K, idx

    if depth > K:
        return
    inorder(now * 2, depth + 1)
    Q[now] = building[idx]
    idx += 1
    inorder(now * 2 + 1, depth + 1)


K = int(input())
building = list(map(int, input().split()))
Q =[0] * (1 << K)
idx = 0
inorder(1, 1)

for i in range(K):
    for j in range(1 << i):
        print(Q[2 ** i + j], end=' ')
    print()