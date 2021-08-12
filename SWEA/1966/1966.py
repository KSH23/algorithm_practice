# 1966. 숫자를 정렬하자


def sort_numbers(n, num_list):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

    return num_list


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    my_num_list = list(map(int, input().split()))
    print('#{}'.format(tc), end=" ")
    for i in range(N):
        print('{}'.format(sort_numbers(N, my_num_list)[i]), end=" ")
    print()