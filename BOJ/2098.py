# 2098. 외판원 순회


import sys


def travel(visited_bit, current_city):
    if memo[current_city][visited_bit]:  # 이미 계산된 경우
        return memo[current_city][visited_bit]

    if visited_bit == (1 << N) - 1:
        # 모든 도시를 방문하면 출발 도시로 돌아가는 비용 반환
        if cost_map[current_city][0]:
            return cost_map[current_city][0]
        # 만약 출발 도시로 돌아갈 수 없다면 문제에서 불가능한 무한대 반환
        return 16000001

    ret = 16000001  # 문제에서 불가능한 무한대
    for city in range(N):
        if visited_bit & (1 << city):  # 이미 방문
            continue
        if not cost_map[current_city][city]:  # 길이 없는 경우
            continue
        ret = min(travel(visited_bit | (1 << city), city) + cost_map[current_city][city], ret)

    memo[current_city][visited_bit] = ret  # 최소 비용 기록
    return ret


N = int(sys.stdin.readline())
cost_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# memo[bit][city]: bit에 표시된 도시를 방문하고 현재 city 도시에 있을 때 쓴 최소 비용
memo = [[0] * (1 << N) for _ in range(N)]

travel(1 << 0, 0)
print(memo[0][1])