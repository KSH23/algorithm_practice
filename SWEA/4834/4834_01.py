# 12458. 숫자 카드


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input()))

    cnt_list = [0] * 10    # 카드 갯수 리스트 생성

    for num in num_list:    # 각 카드 갯수 갱신
        cnt_list[num] += 1

    max_cnt = 0    # 최대 갯수(-1이 더 나음)
    max_num = 0    # 최고 숫자(-2이 더 나음)

    # 최대 카드 갯수와 최고 숫자를 갱신
    for i in range(10):
        if cnt_list[i] >= max_cnt:
            max_cnt = cnt_list[i]
            max_num = i

    print('#{} {} {}'.format(tc, max_num, max_cnt))