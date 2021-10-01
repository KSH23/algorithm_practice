# 15650. N과 M (2)


def perm(limit, perm_list):
    if len(perm_list) == M:
        print(' '.join(map(str, perm_list)))
        return

    for num in range(limit, N + 1):
        if num_check[num] == 1:
            continue
        num_check[num] = 1
        perm(num, perm_list + [num])
        num_check[num] = 0


N, M = map(int, input().split())
num_check = [0] * (N+1)
perm(1, [])