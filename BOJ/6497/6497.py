# 6497. 전력난(Kruskal)


import sys


def find_parent(x):  # x의 조상 반환
    if parents[x] == x:
        return x
    parent = find_parent(parents[x])
    parents[x] = parent
    return parent


while True:
    house_num, load_num = map(int, input().split())
    if house_num + load_num == 0:  # 입력 종료
        break

    # 도로간 연결 관계를 저장
    loads = [list(map(int, sys.stdin.readline().split())) for _ in range(load_num)]
    loads.sort(key=lambda x: x[2])  # 거리 기준 정렬

    parents = list(range(house_num))  # 각 집의 조상 저장

    total_cost = sum(x[2] for x in loads)  # 모든 거리 길이 총 합
    for load in loads:
        house1, house2, length = load
        if find_parent(house1) == find_parent(house2):
            continue  # 이미 같은 조상에 속한 두 집은 고려하지 않음
        parents[find_parent(house2)] = find_parent(house1)  # 두 집의 조상 결합
        total_cost -= length  # 사용한 비용 갱신

    print(total_cost)