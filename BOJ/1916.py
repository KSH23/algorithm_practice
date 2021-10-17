# 1916. 최소비용 구하기


from sys import stdin


def dijkstra(start, end):
    visited = [0] * (N + 1)
    dist = [100000000] * (N + 1)

    dist[start] = 0  # start 지점 비용 초기화

    for _ in range(N):  # N개의 도시를 확정
        # 현재 도시에서 최소 비용으로 갈 수 있는 도시 선정
        min_cost, min_cost_city = 1000000000, 0
        for city in range(1, N + 1):
            if visited[city]:  # 이미 확정된 도시는 무시
                continue
            if dist[city] < min_cost:  # 최소 비용과 도시 갱신
                min_cost = dist[city]
                min_cost_city = city

        visited[min_cost_city] = 1  # 최소 비용으로 갈 수 있는 도시 확정

        # 회소 비용으로 갈 수 있는 도시에서 갈 수 있는 도시들의 비용 갱신
        for next_city, c in bus_map[min_cost_city]:
            if dist[next_city] <= min_cost + c:
                continue  # 지금 도시를 거쳐가는 비용이 더 크다면 무시
            dist[next_city] = min_cost + c

    return dist[end]


N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수
bus_map = [[] for _ in range(N + 1)]  # 버스 정보 저장
for _ in range(M):
    city1, city2, cost = list(map(int, stdin.readline().split()))
    bus_map[city1].append([city2, cost])
s, e = map(int, input().split())  # 출발점과 도착점
print(dijkstra(s, e))