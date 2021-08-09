# 2304. 창고 다각형


def warehouse(col_list):
    # 기둥 높이를 반영한 창고 바닥 리스트를 만든 이후
    # 내림차순으로 정렬된 기둥 높이를 돌면서 
    # 현재 기둥 위치와 다음 기둥 위치 사이의 높이를 두 기둥 중 낮은 기둥 높이로 채움

    # 기둥 높이를 기준으로 내림차순 정렬된 리스트 생성
    check_list = sorted(col_list, key=lambda x: x[1], reverse=True)

    col_list.sort()    # 기둥 리스트를 위치순으로 정렬
    c_list = []    # 기둥의 높이만을 담은 리스트 생성, 창고 바닥을 나타냄
 
    while True:    # 창고 바닥의 높이를 기록, 기둥이 없으면 0, 기둥이 있으면 해당 높이
        if len(col_list) == 0:    # 기존 리스트에서 기둥이 모두 사라지면 break
            break
        elif col_list[0][0] == len(c_list):
            c_list.append(col_list[0][1])    # 기둥이 있으면 그 높이를 넣음
            col_list = col_list[1:]    # 기존의 리스트에서 제거
        else:    
            c_list.append(0)    # 기둥이 없으면 0
  
    for i in range(len(check_list)-1):
        # 현재 기둥 위치와 다음 기둥 위치를 정하는 두 개의 변수
        x1 = min(check_list[i][0], check_list[i+1][0])
        x2 = max(check_list[i][0], check_list[i+1][0])

        # 기둥 사이의 위치들을 돌며 그 높이가 낮은 기둥 높이보다 낮다면 새로 갱신
        for j in range(x1, x2+1):
            if c_list[j] < check_list[i+1][1]:
                c_list[j] = check_list[i+1][1]

    result = sum(c_list)    # 창고 바닥에 적힌 숫자를 모두 더하면 최종 결과

    return result
    

N = int(input())

my_col_list = []
for i in range(N):
    my_col_list.append(list(map(int, input().split())))

print(warehouse(my_col_list))