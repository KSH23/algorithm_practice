# 12015. 가장 긴 증가하는 부분 수열 2


import sys


def binary_search(cur_lis, target):
    # 현재 lis에서 목표 숫자가 들어갈 수 있는 자리 즉,
    # lower bound를 반환하는 함수

    left = 0
    right = len(cur_lis)
    while left <= right:
        mid = (left + right) // 2
        if target < cur_lis[mid]:
            right = mid - 1
        elif cur_lis[mid] < target:
            left = mid + 1
        else:  # l[mid] == target
            return mid

    return left


N = int(sys.stdin.readline())
LIST = list(map(int, sys.stdin.readline().split()))

lis = [LIST[0]]  # 가장 긴 증가하는 부분 수열 리스트

for num in LIST[1:]:
    # 만약 현재 lis의 마지막 숫자보다 크다면 맨 뒤에 추가한다
    # 즉 이때 무조건 LIS의 길이는 증가한다
    if lis[-1] < num:
        lis.append(num)

    # 현재 숫자의 위치를 이분 탐색을 통해 찾고 그 위치에 넣는다
    else:
        idx = binary_search(lis, num)
        lis[idx] = num
print(len(lis))  # 길이 출력