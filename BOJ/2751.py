# 2751. 수 정렬하기 2(merge sort)


import sys


def merge(left, right):
    result = []  # 병합 결과를 담는 리스트
    i, j = 0, 0  # left와 right의 인덱스

    while i < len(left) or j < len(right):
        # 두 리스트 모두 확인하지 않는 경우 더 작은 원소를 차례로 추가
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif i < len(left):  # 좌측 리스트를 모두 확인 못한 경우
            result += left[i:]
            break
        else:  # 우측 리스트를 모두 확인 못한 경우
            result += right[j:]
            break

    return result


def merge_sort(num_list):
    if len(num_list) == 1:  # 숫자가 한 개 남은 경우
        return num_list

    # 리스트를 좌우로 나누어 병합 정렬 진행
    left_list = merge_sort(num_list[:len(num_list) // 2])
    right_list = merge_sort(num_list[len(num_list) // 2:])

    # 두 리스트를 병합한 결과 반환
    return merge(left_list, right_list)


N = int(input())
numbers = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
sorted_numbers = merge_sort(numbers)
for number in sorted_numbers:
    print(number)