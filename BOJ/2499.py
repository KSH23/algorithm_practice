# 2499. 저울


def possible_weight(weight_list):
    # 추를 무게에 따라 오름차순으로 정렬
    for i in range(len(weight_list) - 1):
        for j in range(i + 1, len(weight_list)):
            if weight_list[i] > weight_list[j]:
                weight_list[i], weight_list[j] = weight_list[j], weight_list[i]
    
    # 만들 수 있는 최소 무게는 특정 지점까지의 합이 그 다음 요소보다 작을 때,
    # 또는 가장 가벼운 추의 무게가 1이 아닐 때이다.
    number_sum = weight_list[0]    # 가장 가벼운 추의 무게 저장
    
    # 만약 가장 가벼운 추의 무게가 1이 아니라면 1을 return
    if number_sum != 1:
        return 1
    
    # n-1번까지의 추의 합이 n번 추보다 작다면 합 + 1이 답이 된다
    for i in range(1, len(weight_list)):
        if number_sum + 1 < weight_list[i]:
            return number_sum + 1
        else:
            number_sum += weight_list[i]
            
    # 위 두 경우에 해당되지 않는다면 모든 추 무게의 합 + 1이 답이 된다
    return number_sum + 1


N = int(input())
my_weight_list = list(map(int, input().split()))
print(possible_weight(my_weight_list))