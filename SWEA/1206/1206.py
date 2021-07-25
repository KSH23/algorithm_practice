"""
1206: View
"""

import sys
sys.stdin = open('1206_input.txt')


def find_view(building_list, length):
    view = 0
    for idx in range(2, length - 2):
        # 좌측에서 얻을 수 있는 가장 큰 view 값
        left_view = building_list[idx] - max(building_list[idx-1], building_list[idx-2])

        # 만약 이 값이 음수가 나온다면 0으로 바꿔줌
        if left_view <= 0:
            left_view = 0

        # 우측에서 얻을 수 있는 가장 큰 view 값
        right_view = building_list[idx] - max(building_list[idx+1], building_list[idx+2])
        if right_view <= 0:
            right_view = 0
        
        # 좌측과 우측에서 얻을 수 있는 view 값 중 작은 것을 택함
        view += min(left_view, right_view)

    return view


T = 10

for tc in range(1, T+1):
    my_length = int(input())
    my_building_list = list(map(int, input().split()))
    # print(my_building_list)
    # print(my_length)

    print(f'#{tc} {find_view(my_building_list, my_length)}')