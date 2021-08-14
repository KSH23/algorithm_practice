# 2564. 경비원


def guard(col, row, shops, location):
    idx = 0    # 현재 경비원이 있는 방향을 담을 변수
    d = [1, 4, 2, 3]    # 상점 위치를 시계방향으로 담음
    for i in range(4):    # 현재 경비원의 방향 인덱스를 결정
        if location[0] == d[i]:
            idx = i

    distance = 0    # 총 거리를 담을 변수
    for shop in shops:
        # 현재 위치(idx)에서 왼쪽 상점까지 가능한 모든 거리의 경우의 수를 담음
        your_left = [
            col - location[1] + shop[1],
            row - location[1] + col - shop[1],
            location[1] + row - shop[1],
            location[1] + shop[1]
        ]

        # 마찬가지로 오른쪽 상점까지 가능한 모든 거리의 경우의 수를 담음
        your_right = [
            location[1] + shop[1],
            location[1] + col - shop[1],
            col - location[1] + row - shop[1],
            row - location[1] + shop[1]
        ]

        temp_distance = 0    # 각 상점까지의 거리를 담을 변수

        if shop[0] == d[(idx + 2) % 4]:    # 맞은편에 있는 상점
            if shop[1] <= col - location[1]:    # 시계방향이 짧은 경우
                temp_distance += location[1] + row + shop[1]
            else:    # 반시계방향이 짧은 경우
                temp_distance += col - location[1] + row + col - shop[1]

        elif shop[0] == location[0]:    # 같은편에 있는 상점은 절댓값 구함
            if shop[1] <= location[1]:
                temp_distance += location[1] - shop[1]
            else:
                temp_distance += shop[1] - location[1]

        elif shop[0] == d[(idx + 1) % 4]:    # 왼편에 있는 상점
            temp_distance = your_left[idx]    # 위 리스트에서 해당 값을 가져옴

        else:    # 오른편에 있는 상점
            temp_distance = your_right[idx]    # 위 리스트에서 해당 값을 가져옴

        distance += temp_distance    # 총 거리에 추가

    return distance


COL, ROW = map(int, input().split())
shop_n = int(input())
# 1북 2남 3서 4동
my_shops = [list(map(int, input().split())) for _ in range(shop_n)]
my_location = list(map(int, input().split()))

print(guard(COL, ROW, my_shops, my_location))