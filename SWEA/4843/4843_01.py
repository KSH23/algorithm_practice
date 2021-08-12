# 4843. 특별한 정렬


def special_sort(n, num_list):
    result = []

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if num_list[j] < num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

    while len(result) != 10:
        result += [num_list[0]]
        result += [num_list[-1]]
        num_list = num_list[1: -1]

    return result


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    my_list = list(map(int, input().split()))

    result_list = ' '.join(map(str, special_sort(N, my_list)))
    print('#{} {}'.format(tc, result_list))