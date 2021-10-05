# 10974. 모든 순열


def perm(perm_list):
    if len(perm_list) == N:
        print(' '.join(map(str, perm_list)))
        return

    for num in range(1, N + 1):
        if num_check[num] == 1:
            continue
        num_check[num] = 1
        perm(perm_list + [num])
        num_check[num] = 0


N = int(input())
num_check = [0] * (N+1)
perm([])