# 12533. 델타검색 응용


def delta_search(n, num_list):
    di = [-2, -1, -2, -1, 2, 2, 1, 1]
    dj = [-1, -2, 1, 2, -1, 1, 2, -2]
    total_sum = 0

    for i in range(n):
        for j in range(n):
            for cnt in range(8):
                if i + di[cnt] < 0 or n <= i + di[cnt] or j + dj[cnt] < 0 or n <= j + dj[cnt]:
                    continue
                temp_sum = num_list[i][j] - num_list[i + di[cnt]][j + dj[cnt]]
                if temp_sum > 0:
                    total_sum += temp_sum
                else:
                    total_sum -= temp_sum
    return total_sum


for tc in range(1, 11):
    N = int(input())
    my_num_list = [list(map(int, input().split())) for _ in range(N)]

    print('#{} {}'.format(tc, delta_search(N, my_num_list)))