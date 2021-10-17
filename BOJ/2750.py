# 2750. 수 정렬하기(quick sort)


import sys

sys.setrecursionlimit(100000)


def partition(num_list, start, end):
    pivot = num_list[start]
    left = start + 1  # 좌측 인덱스
    right = end  # 우측 인덱스

    while left <= right:
        # pivot보다 작은 값이라면 좌측 인덱스 증가
        while left <= right and num_list[left] <= pivot:
            left += 1

        # pivot보다 큰 값이라면 우측 인덱스 감소
        while left <= right and pivot <= num_list[right]:
            right -= 1

        # 이동한 결과 마지막으로 지정된 원소를 서로 swap
        if left <= right:
            num_list[left], num_list[right] = num_list[right], num_list[left]

    # swap이 모두 종료되면 right 인덱스 원소가 left 인덱스 원소보다 작게 됨
    num_list[right], num_list[start] = num_list[start], num_list[right]
    return right


def quick_sort(num_list, start, end):
    if start < end:
        pivot = partition(num_list, start, end)
        quick_sort(num_list, start, pivot - 1)
        quick_sort(num_list, pivot + 1, end)
    return num_list


N = int(input())
numbers = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
sorted_numbers = quick_sort(numbers, 0, N - 1)
for number in sorted_numbers:
    print(number)