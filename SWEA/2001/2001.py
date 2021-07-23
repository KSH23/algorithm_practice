"""
2001: 파리 퇴치
"""

import sys
sys.stdin = open('2001_input.txt')


# 파리채가 잡는 파리 수를 센 후 가장 큰 수를 return하는 함수 
def flyflapper(flapper_size, space):
    space_length = len(space[0])
    
    total_dead_fly = []

    # space를 vertical, horizontal로 돌아
    for ver_space in range(space_length - (flapper_size - 1)):
        for hor_space in range(space_length - (flapper_size - 1)):
            dead_fly = 0

            # flapper_size의 정사각형을 돌며 파리 수 더해
            for i in range(ver_space, ver_space + flapper_size):
                for j in range(hor_space, hor_space + flapper_size):
                    dead_fly += int(space[i][j])
            # print(dead_fly)
            
            # 죽은 파리 수를 리스트에 담아
            total_dead_fly += [dead_fly]

    # 죽은 파리 수 리스트 중 가장 큰 수 return
    return max(total_dead_fly)


T = int(input())

for tc in range(1, T+1):
    dimension = []
    n, m =  map(int, input().split())
    # print('---------', n, m)

    # input 받은 값을 토대로 공간 생성
    for i in range(n):
        dimension.append(list((input().split())))
   
    # print(dimension)

    print(f'#{tc} {flyflapper(m, dimension)}')