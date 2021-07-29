"""
1211: Ladder2
"""

import sys
sys.stdin = open('1211_input.txt')


def short_ladder(ladder):
    # 모든 경우의 수를 세고 그 결과를 담을 리스트 생성
    distance_list = []

    # 막대들의 index 값을 따로 저장
    sticks = []
    for ii in range(100):
        if ladder[0][ii] == 1:
            sticks.append(ii)

    # 막대기들 수 만큼 반복할 예정
    for stick_idx in range(len(sticks)):
        distance = 0    # 거리를 담는 변수
        my_stick = stick_idx    # 현재 막대기의 인덱스 값

        # 초기 위치 좌표 설정
        # x는 가로줄, y는 세로줄
        x = y = 0   
        
        # 하나의 막대기마다 아래로 100칸 내려가야 하니까 100번 반복할 예정
        for i in range(100):      
            # x 좌표를 막대기 위치로 변경     
            x = sticks[my_stick]   

            # 막대기가 왼쪽 벽에 붙은 경우
            if x == 0:
                if ladder[y][x + 1] == 1:
                    # 1이 발견되면 그 방향으로 막대기를 건너간다
                    my_stick += 1
                    # 건너간 만큼 이동 거리 증가
                    distance += sticks[my_stick] - sticks[my_stick - 1] 
                   
            # 막대기가 오른쪽 벽에 붙은 경우
            elif x == 99:
                if ladder[y ][x - 1] == 1:
                    my_stick -= 1
                    distance += sticks[my_stick + 1] - sticks[my_stick] 
                          
            # 막대기가 벽에 붙지 않았다면 양 쪽 다 확인
            else: 
                if ladder[y][x + 1] == 1:
                    my_stick += 1                
                    distance += sticks[my_stick] - sticks[my_stick - 1] 
                                   
                elif ladder[y][x - 1] == 1:
                    my_stick -= 1
                    distance += sticks[my_stick + 1] - sticks[my_stick] 

            # 위 조건들을 끝내면 항상 아래로 한 칸씩 이동       
            y += 1
            distance += 1

        distance_list.append(distance)

    # 여기까지 오면 이동 거리들이 담긴 리스트가 완성됨
    # 이제 가장 최소 거리를 구하고 그에 해당하는 인덱스를 구할 것
    min_index = 0    # 최소 거리의 인덱스 값
    min_distance = distance_list[0]    # 최소 거리 변수
 
    # 리스트 돌면서 최소 거리 구하고 그 때의 인덱스 값 구함
    for i in range(len(distance_list)):
        if distance_list[i] < min_distance:
            min_distance = distance_list[i]
            min_index = sticks[i]

    return min_index


T = 10

for tc in range(1, T+1):
    no = int(input())

    # 사다리 행렬 만들기
    my_ladder = []
    for i in range(100):
        my_ladder.append(list(map(int, input().split())))

    print(f'#{no} {short_ladder(my_ladder)}')