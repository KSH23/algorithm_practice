# 5205. 퀵 정렬


def partition(num_list, start, end):
    pivot = num_list[start]
    left = start + 1
    right = end
    while left <= right:
        while left <= right and num_list[left] <= pivot:
            left += 1
        while left <= right and num_list[right] >= pivot:
            right -= 1
        if left <= right:
            num_list[left], num_list[right] = num_list[right], num_list[left]

    num_list[right], num_list[start] = num_list[start], num_list[right]
    return right


def quick_sort(num_list, start, end):
    if start < end:
        pivot = partition(num_list, start, end)
        quick_sort(num_list, start, pivot - 1)
        quick_sort(num_list, pivot + 1, end)
    return num_list


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    my_num_list = list(map(int, input().split()))
    print(f'#{tc} {quick_sort(my_num_list, 0, N - 1)[N // 2]}')