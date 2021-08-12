# 4837. 부분집합의 합


def subset_sum(n, k):
    num_list = list(range(1, 13))
    cnt = 0
    for i in range(1 << 12):
        temp_set = []
        for j in range(12):
            if (1 << j) & i != 0:
                temp_set += [num_list[j]]

        if len(temp_set) == n:
            temp_sum = 0
            for l in range(n):
                temp_sum += temp_set[l]
            if temp_sum == k:
                cnt += 1

    return cnt


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    print('#{} {}'.format(tc, subset_sum(N, K)))
