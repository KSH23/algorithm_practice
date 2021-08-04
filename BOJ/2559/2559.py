# 2559. 수열


def max_temp(n, k, temp_list):
    # 최종 결과, 각 단계의 결과를 담는 변수 초기화
    max_result = temp_max = sum(temp_list[0: k])

    for i in range(n - k):
        # 현 단계의 결과는 전 단계 결과에서 맨 앞 요소를 빼고 맨 뒤 이후 다음 요소를 더한 것
        temp_max = temp_max - temp_list[i] + temp_list[k + i]
        if temp_max > max_result:
            max_result = temp_max
    

    return max_result


N, K = map(int, input().split())
my_temp_list = list(map(int, input().split()))

# print(N, K, my_temp_list)
print(max_temp(N, K, my_temp_list))