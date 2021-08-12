# 1966. 숫자를 정렬하자(선택정렬 이용)


def sort_numbers(n, num_list):
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if num_list[j] < num_list[min_idx]:
                min_idx = j
        num_list[min_idx], num_list[i] = num_list[i], num_list[min_idx]

    return num_list


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    my_num_list = list(map(int, input().split()))
    print('#{}'.format(tc), end=" ")
    for i in range(N):
        print('{}'.format(sort_numbers(N, my_num_list)[i]), end=" ")
    print()