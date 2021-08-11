# 12523. 델타검색


def delta_search(n, num_list):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    total_sum = 0

    for i in range(n):
        for j in range(n):
            for cnt in range(4):
                if 0 <= i + di[cnt] and i + di[cnt] < n and 0 <= j + dj[cnt] and j + dj[cnt] < n:
                    temp_sum = num_list[i][j] - num_list[i + di[cnt]][j + dj[cnt]]
                    if temp_sum > 0:
                        total_sum += temp_sum
                    else:
                        total_sum -= temp_sum
    return total_sum


for tc in range(1, 11):
    N = int(input())
    my_num_list = []
    for i in range(N):
        my_num_list += [list(map(int, input().split()))]

    print('#{} {}'.format(tc, delta_search(N, my_num_list)))