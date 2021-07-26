"""
1208: Flatten
"""

import sys
sys.stdin = open('1208_input.txt')


def dump(count, boxes):
    while count > 0:    
        # 최대, 최소 박스 높이와 각각의 index 값 저장
        max_box = boxes[0]
        max_box_idx = 0
        min_box = boxes[0]
        min_box_idx = 0
        
        # while 한 번 돌때마다 최대, 최소 높이와 각각의 index 갱신
        for idx in range(len(boxes)):
            if max_box < boxes[idx]:
                max_box = boxes[idx]
                max_box_idx = idx
   
            elif boxes[idx] < min_box:
                min_box = boxes[idx]
                min_box_idx = idx
        
        # 박스 높이가 음수가 되지 않도록 유지하면서
        # 최대 높이를 한 칸 줄이고, 최소 높이를 한 칸 늘림
        if boxes[max_box_idx] > 0 and boxes[min_box_idx] >= 0:
            boxes[max_box_idx] -= 1
            boxes[min_box_idx] += 1
        else: 
            break

        count -= 1

    return max(boxes) - min(boxes)


T = 10

for tc in range(1, T+1):
    dump_count = int(input())
    boxes_list = list(map(int, input().split()))

    print(f'#{tc} {dump(dump_count, boxes_list)}')