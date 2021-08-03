# 2304. 창고 다각형


def warehouse(w_list):
    w_list.sort()    # 받은 리스트를 좌표순으로 정렬
    max_height = 0    # 건물 최대 높이

    for w in w_list:
        if w[1] > max_height:
            max_height = w[1]    # 건물 최대 높이 구함
      
    # 최대 높이를 기준으로 좌우 따로 구할 예정
    area = max_height

    # 가장 높은 기둥 왼쪽의 면적을 구할 예정
    local_max = w_list[0][1]
    local_m_i = w_list[0][0]
    i = 0
    while True:
        if w_list[i][1] == max_height:
            area += (w_list[i][0] - local_m_i) * local_max
            break
        elif w_list[i][1] > local_max:
            area += (w_list[i][0] - local_m_i) * local_max
            local_max = w_list[i][1]
            local_m_i = w_list[i][0]
        i += 1
    
    i = 0
    local_max = w_list[-1][1]
    local_m_i = w_list[-1][0]
    while True:
        if w_list[-1-i][1] == max_height:
            area += (local_m_i - w_list[-1-i][0]) * local_max
            break

        elif w_list[-1-i][1] > local_max:
            area += (local_m_i - w_list[-1-i][0]) * local_max
            local_max = w_list[-1-i][1]
            local_m_i = w_list[-1-i][0]
            
        i += 1

    return area

    
N = int(input())

my_w_list = []
for i in range(N):
    my_w_list.append(list(map(int, input().split())))

print(warehouse(my_w_list))