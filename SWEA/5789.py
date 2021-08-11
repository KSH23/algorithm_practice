# 5789. 현주의 상자 바꾸기


def change_box(box_list, num, l, r):
    for i in range(l-1, r):
        box_list[i] = num
    return box_list


T = int(input())

for tc in range(1, T+1):
    N, Q = list(map(int, input().split()))
    my_box_list = [0]*N
    for i in range(1, Q+1):
        L, R = list(map(int, input().split()))
        my_box_list = change_box(my_box_list, i, L, R)

    print('#{} {}'.format(tc, ' '.join(map(str, my_box_list))))
