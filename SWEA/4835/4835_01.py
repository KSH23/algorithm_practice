# 12459. 구간합


T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    
    # 최댓값과 최솟값은 둘 다 가장 첫번째 경우로 초기화
    max_value = min_value = 0
    for i in range(M):
        max_value += num_list[i]
        min_value += num_list[i]

    # i를 하나씩 증가시키며 M칸씩 더한 후 최대, 최소 비교
    for i in range(N-M+1):
        temp = 0
        for j in range(M):
            temp += num_list[i + j]
        if temp > max_value:
            max_value = temp
        elif temp < min_value:
            min_value = temp

    print('#{} {}'.format(tc, max_value-min_value))