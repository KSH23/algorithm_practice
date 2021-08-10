# 1206. View


for tc in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))
    # print(building)
    sum = 0
    for i in range(2, N-2):    # 2에서 N-3까지 돌 예정
        max_value = 0
        for j in range(-2, 3):    # -2에서 2까지 돌 예정
            if j != 0 and max_value < building[i + j]:
                max_value = building[i + j]

        ret = building[i] - max_value    # i번째 빌딩의 조망권
        if ret < 0:
            ret = 0
        sum += ret

    print("#{} {}".format(tc, sum))