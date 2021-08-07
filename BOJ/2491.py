# 2491. 수열


def find_sequence(n, num_list):
    as_count = 1    # 오름차순 최대 길이
    de_count = 1    # 내림차순 최대 길이

    temp_count = 1
    for i in range(n - 1):    # 오름차순 확인
        if num_list[i] <= num_list[i+1]:
            temp_count += 1
        else:    # 오름차순이 끊기면 1로 초기화
            temp_count = 1

        if as_count < temp_count:
            as_count = temp_count
    
    temp_count = 1
    for i in range(n - 1):    # 내림차순 확인
        if num_list[i] >= num_list[i+1]:
            temp_count += 1
        else:    # 내림차순이 끊기면 1로 초기화
            temp_count = 1
        
        if de_count < temp_count:
            de_count = temp_count
   
    return max(as_count, de_count)
                

N = int(input())

my_num_list = list(map(int, input().split()))

print(find_sequence(N, my_num_list))