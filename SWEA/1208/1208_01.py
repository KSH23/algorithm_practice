# 1208. Flatten


def flatten(dump, box_list):
    while dump >= 0:
        # 가장 높고 낮은 박스의 높이와 인덱스 초기화
        low_box = high_box = box_list[0]
        low_idx = high_idx = 0
        
        # 박스들을 돌며 최고/최저를 찾아 변수들을 갱신
        for i in range(len(box_list)):
            if high_box <= box_list[i]:
                high_box = box_list[i]
                high_idx = i
            elif box_list[i] < low_box:
                low_box = box_list[i]
                low_idx = i
        
        # dump 1회 진행
        box_list[high_idx] -= 1
        box_list[low_idx] += 1
        dump -= 1

    return high_box - low_box


T = 10
for tc in range(1, T+1):
    total_dump = int(input())
    my_box_list = list(map(int, input().split()))
    print('#{} {}'.format(tc, flatten(total_dump, my_box_list)))