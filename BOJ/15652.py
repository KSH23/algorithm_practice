# 15652. N과 M (4)


def perm(limit, perm_list):
    if len(perm_list) == M:
        print(' '.join(map(str, perm_list)))
        return

    for num in range(limit, N + 1):
        perm(num, perm_list + [num])


N, M = map(int, input().split())
perm(1, [])