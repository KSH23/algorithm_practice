# 6497. 전력난(Prim)


import sys
import heapq


def prim():
    hq = []  # heapq
    heapq.heappush(hq, [0, 0])  # 0번 집으로 시작 지점 추가
    lengths = [1 << 31] * house_num  # 해당 집으로 가기 위해 선택된 거리
    lengths[0] = 0  # 시작 지점 초기화
    visited = [0] * house_num

    while hq:
        cur_length, cur_house = heapq.heappop(hq)
        if visited[cur_house]:  # 이미 방문한 집
            continue
        visited[cur_house] = 1  # 방문 표시

        for n_length, n_house in loads[cur_house]:
            if visited[n_house]:
                continue  # 이미 방문한 집
            if lengths[n_house] <= n_length:
                continue  # 가는게 손해인 집
            lengths[n_house] = n_length  # 거리 갱신
            heapq.heappush(hq, [n_length, n_house])

    return sum(lengths)


while True:
    house_num, load_num = map(int, input().split())
    if house_num + load_num == 0:  # 입력 종료
        break

    # 도로간 연결 관계를 거리 기준으로 저장
    loads = [[] for _ in range(house_num)]
    total_cost = 0  # 모든 거리 길이 총 합
    for _ in range(load_num):
        house1, house2, length = map(int, sys.stdin.readline().split())
        total_cost += length
        loads[house1].append([length, house2])
        loads[house2].append([length, house1])

    total_cost -= prim()  # 사용한 비용 차감

    print(total_cost)