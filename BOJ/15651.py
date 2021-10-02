# 15651. N과 M (3)


def perm(perm_list):
    if len(perm_list) == M:
        print(' '.join(map(str, perm_list)))
        return

    for num in range(1, N + 1):
        perm(perm_list + [num])


N, M = map(int, input().split())
perm([])