# 1647. 도시 분할 계획


import sys
import heapq


def find(x):
    # x의 조상을 찾아서 반환
    if parents[x] == x:
        return x

    p_x = find(parents[x])
    parents[x] = p_x
    return p_x


N, M = map(int, sys.stdin.readline().split())
edges = []  # 길 저장 힙
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    heapq.heappush(edges, (C, A, B))  # 유지비를 기준으로 저장

parents = list(range(N + 1))  # 각 집의 조상 저장

max_cost = 0  # 가장 유지비가 큰 도로
total_cost = 0  # 총 유지비

while edges:
    cost, house1, house2 = heapq.heappop(edges)

    # 이미 형성된 마을에 포함된 집은 무시
    if find(house1) == find(house2):
        continue

    # house1과 house2를 하나의 마을로 합침
    parents[find(house2)] = find(house1)
    total_cost += cost
    max_cost = cost

city_cnt = 0  # 마을의 개수
for idx in range(1, N + 1):
    if parents[idx] == idx:
        city_cnt += 1

# 만약 마을이 2개 만들어졌다면 유지비 출력
if city_cnt == 2:
    print(total_cost)

# 만약 모든 집이 하나의 마을로 포함되면 최고 유지비 길 제거
elif city_cnt == 1:
    print(total_cost - max_cost)