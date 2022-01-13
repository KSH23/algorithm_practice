# 17404. RGB거리 2


import sys

N = int(sys.stdin.readline())

# cost[1번 집의 색][현재 집의 색] = 필요한 최종 최소 비용
cost = [[1001 * N] * 3 for _ in range(3)]

# 첫번째 집을 칠하며 cost 리스트에 해당 값을 기록
R, G, B = map(int, sys.stdin.readline().split())
cost[0][0] = R
cost[1][1] = G
cost[2][2] = B

for _ in range(N - 1):
    # 현재 집을 칠하기 위해 필요한 비용
    color_list = list(map(int, sys.stdin.readline().split()))
    
    # 현재 집을 칠하는 모든 경우의 수의 비용 임시 저장 리스트
    temp_cost = [[1001 * N] * 3 for _ in range(3)]

    for first_house in range(3):  # 1번 집의 색
        for paint in range(3):  # 현재 집에 칠할 색
            for pre_house in range(3):  # 이전 집에 칠한 색
                if pre_house == paint:  # 이전 집과 같은 색은 칠할 수 없음
                    continue
                # 현재 칠할 수 있는 색 중 최소 비용의 색을 갱신
                temp_cost[first_house][paint] = min(temp_cost[first_house][paint],
                                                    cost[first_house][pre_house] + color_list[paint])
    cost = temp_cost[:]  # 현재 집을 칠하는 최소 비용을 최종 비용 리스트에 복사

ans = 1001 * N
# 마지막집 까지 칠한 뒤 마지막 집과 첫번째 집의 색이 같지 않은 경우중 최소 비용 도출
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        ans = min(cost[i][j], ans)
print(ans)
