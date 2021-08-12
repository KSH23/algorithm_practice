# 4843. 특별한 정렬(선택정렬 이용)


def special_sort(num_list):
    for i in range(len(num_list) - 1):
        if i % 2 == 0:
            max_idx = i
            for j in range(i + 1, len(num_list)):
                if num_list[j] > num_list[max_idx]:
                    max_idx = j
            num_list[max_idx], num_list[i] = num_list[i], num_list[max_idx]

        else:
            min_idx = i
            for j in range(i + 1, len(num_list)):
                if num_list[j] < num_list[min_idx]:
                    min_idx = j
            num_list[min_idx], num_list[i] = num_list[i], num_list[min_idx]

    return num_list[:10]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    my_list = list(map(int, input().split()))

    result_list = ' '.join(map(str, special_sort(my_list)))
    print('#{} {}'.format(tc, result_list))