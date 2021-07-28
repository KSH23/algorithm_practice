"""
1210: Ladder1
"""

import sys
sys.stdin = open('1210_input.txt')


def ladder_winner(ladder):
    # 2가 적힌곳의 행을 알아내 변수에 저장
    winner_x = ladder[99].index(2)
    
    # 시작 위치
    x, y = winner_x, 99

    # 막대들의 index 값을 따로 저장
    sticks = []
    for i in range(100):
        if ladder[0][i] == 1:
            sticks.append(i)
    # 현재 내 막대기의 idx 값을 따로 저장
    my_stick = sticks.index(winner_x)

    # 맨 아래의 시작 위치에서 위로 한 칸씩 올라가면서 확인
    for i in range(100):
        # 막대기가 왼쪽 벽에 붙은 경우
        if x == 0:
            if ladder[y - i][x + 1] == 1:
                # 1이 발견되면 그 방향으로 막대기를 건너간다
                my_stick += 1    
                # 건너간 막대기의 x값을 위에서 구한 리스트에서 구함
                x = sticks[my_stick]

        # 막대기가 오른쪽 벽에 붙은 경우
        elif x == 99:
            if ladder[y - i][x - 1] == 1:
                my_stick -= 1
                x = sticks[my_stick]
        
        # 막대기가 벽에 붙지 않았다면 양 쪽 다 확인
        else: 
            if ladder[y - i][x + 1] == 1:
                my_stick += 1
                x = sticks[my_stick]
            
            elif ladder[y - i][x - 1] == 1:
                my_stick -= 1
                x = sticks[my_stick]

    return x

T = 10

for tc in range(1, T+1):
    no = int(input())

    # 사다리 행렬 만들기
    my_ladder = []
    for i in range(100):
        my_ladder.append(list(map(int, input().split())))

    print(f'#{no} {ladder_winner(my_ladder)}')

    