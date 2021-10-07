# 5207. 이진 탐색


def binary_search(num_list, target):
    left, right = 0, N - 1
    switch = -1  # 초기값을 -1로 설정
    while left <= right:
        m = (left + right) // 2
        if num_list[m] < target and abs(switch) == 1:  # switch가 1이거나 -1일때 가능
            left = m + 1
            switch = 0
        elif num_list[m] > target and switch <= 0:  # switch가 0이거나 -1일때 가능
            right = m - 1
            switch = 1
        elif num_list[m] == target:
            return 1
        else:  # 아무것도 하지 못하는 경우
            break
    return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    my_list = list(map(int, input().split()))
    my_list.sort()  # 리스트 정렬
    target_list = list(map(int, input().split()))
    ans = 0  # 최종 정답
    for t in target_list:
        ans += binary_search(my_list, t)
    print(f'#{tc} {ans}')