# 2304. 창고 다각형


def warehouse(col_list):
    col_list.sort()    # 기둥 리스트를 위치순으로 정렬
    c_list = []    # 기둥의 높이만을 담은 리스트 생성
    while True:
        if len(col_list) == 0:
            break
        elif col_list[0][0] == len(c_list):
            c_list.append(col_list[0][1])
            col_list = col_list[1:]
        else:    
            c_list.append(0)    # 기둥이 없으면 0
  
    x, y = 0, c_list[0]    # 현재 위치 초기화
    
    result = 0    # 최종 면적 결과
    # print(len(c_list) - 1, c_list[-1])
    for x in range(len(c_list) - 1):
        print(x, c_list[x+1:])
        # 만약 c_list[x+1:]의 최댓값이 y보다 크다면
        # 그 최댓값의 idx와 x의 차이와 y의 곱을 면적에 추가
        if y <= max(c_list[x+1:]):
            
            # print(c_list.index(max(c_list[x+1:])), y)
            print(y)
            result += y
        # 만약 c_list[x+1:]의 최댓값이 y보다 작다면
        # 그 최댓값의 idx와 x의 차이와 최댓값의 곱을 면적에 추가
        elif y > max(c_list[x+1:]):
            # print(c_list.index(max(c_list[x+1:])))
            print(max(c_list[x+1:]))
            result += max(c_list[x+1:])

    return result
    


    
N = int(input())

my_col_list = []
for i in range(N):
    my_col_list.append(list(map(int, input().split())))

print(warehouse(my_col_list))