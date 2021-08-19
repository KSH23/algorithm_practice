# 4837. 부분집합 합


def subset_sum(n, num_list):
    check_list = []
    for i in range(1<<n):
        temp_list = []
        for j in range(n):
            if i & (1<<j):
                temp_list += [num_list[j]]
        check_list += [temp_list]

    cnt = 0
    for li in check_list:
        temp_sum = 0
        for ele in range(len(li)):
            temp_sum += li[ele]
        if temp_sum == 0:
            cnt += 1

    return cnt


for tc in range(1, 11):
    N = int(input())
    my_num_list = list(map(int, input().split()))

    print(f'#{tc} {subset_sum(N, my_num_list)}')