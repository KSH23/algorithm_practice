"""
1220: Magnetic
"""

import sys
sys.stdin = open('1220_input.txt')


def magnetic_hole(magnetic):
    # N극은 1, S극은 2
    # 위는 1, 아래는 2 / 위에 2가 닿으면 사라지고 아래에 1이 닿으면 사라짐
    # 1과 2가 붙어있으면 교착상태

    # 주어진 자석 그리드를 세로줄로 나눠 저장할 예정
    vertical_lines = []

    for h in range(len(magnetic[0])):
        temp = []    # 한 줄씩 저장할 임시 리스트
        for v in range(len(magnetic)):
            if magnetic[v][h] != 0:
                temp.append(magnetic[v][h])
        vertical_lines.append(temp)

    count = 0    # 교착상태 갯수

    # 한 줄 한 줄 돌면서 숫자 정리 후 교착상태 수를 셀 예정
    for i in range(len(vertical_lines)):
        # 생성된 모든 세로줄에서 앞에 있는 2, 뒤에 있는 1 다 없애는 while
        while True:
            # 맨 앞이 2면 없애고
            if vertical_lines[i][0] == 2:
                vertical_lines[i] = vertical_lines[i][1:]
            # 맨 뒤가 1이면 없애고
            elif vertical_lines[i][-1] == 1:
                vertical_lines[i] = vertical_lines[i][:-1]
            # 둘 다 아니면 끝내기
            else:
                break
    
        # 위에서부터 기록한 세로줄이므로 리스트에 [1, 2]가 있으면 하나의 교착상태
        # 맨 앞부터 교착상태를 기록하며 제거해 나갈 예정
        while True:
            # 계속 제거해 빈 리스트만 남으면 break
            if len(vertical_lines[i]) == 0:
                break
            else:
                # 만약 [1, 2, ...]이면 교착상태 하나 추가하고 리스트에서 없앰
                if vertical_lines[i][0] == 1 and vertical_lines[i][1] == 2:
                    count += 1
                    vertical_lines[i] = vertical_lines[i][2:]

                # 만약 교착상태도 아닌데 앞에 1이나 2가 있으면 리스트에서 없앰
                elif vertical_lines[i][0] == 1 or vertical_lines[i][0] == 2:
                    vertical_lines[i] = vertical_lines[i][1:]
                    
    return count


T = 10

for tc in range(1, T+1):
    length = int(input())

    my_magnetic = []

    # 자석 그리드 생성
    for i in range(length):
        my_magnetic.append(list(map(int, input().split())))

    print(f'#{tc} {magnetic_hole(my_magnetic)}')