"""
2805: 농작물 수확하기
"""

import sys
sys.stdin = open('2805_input.txt')


def produce(n, farm):
    result = 0

    # 0번줄, -1번줄은 1개 [2]
    # 1번줄, -2번줄은 3개 [1][2][3]
    # n//2 + 1번줄은 n개
    
    # 0번 줄부터 (n // 2)번 줄까지 돌 예정
    for i in range(n // 2 + 1):
        # 가로 칸은 1, 3, 5, ... 개씩 더할 예정
        for j in range(n // 2 -i, n // 2 + i+1):
            # 만약 정 가운데 줄이라면 그 줄 전체를 더함
            if i == n // 2:
                result += farm[i][j]

            # 그렇지 않다면 위, 아래 줄의 칸을 동시에 더함(상하 대칭)
            else:
                result += farm[i][j] + farm[-1 -i][j]
               
    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 농장 그리드 형성
    my_farm = []
    for i in range(N):
        my_farm.append(list(map(int, input())))

    print(f'#{tc} {produce(N, my_farm)}')