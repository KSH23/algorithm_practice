# 5204. 병합 정렬


def merge(left, right):
    global cnt

    if left[-1] > right[-1]:
        cnt += 1

    i = 0  # left 리스트의 인덱스
    j = 0  # right 리스트의 인덱스
    result = []  # 병합한 결과를 담는 리스트

    while i < len(left) or j < len(right):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif i < len(left):  # left 리스트에 남은 원소가 있는 경우
            result += left[i:]
            break
        else:  # right 리스트에 남은 원소가 있는 경우
            result += right[j:]
            break

    return result


def merge_sort(some_list):
    if len(some_list) == 1:
        return some_list

    left_list = merge_sort(some_list[0: len(some_list) // 2])
    right_list = merge_sort(some_list[len(some_list) // 2:])

    return merge(left_list, right_list)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    cnt = 0  # 병합 과정에서 left[-1] > right[-1]가 되는 경우의 수
    ans = merge_sort(num_list)
    print(f'#{tc} {ans[N // 2]} {cnt}')