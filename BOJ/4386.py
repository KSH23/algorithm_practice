# 4386. 별자리 만들기


import sys
import heapq


def find(child):
    # 조상을 찾아 이를 조상 리스트에 저장하고 반환
    if parents[child] == child:
        return child

    parent = find(parents[child])
    parents[child] = parent
    return parent


N = int(sys.stdin.readline())
stars = []  # 별의 좌표 저장
for _ in range(N):
    x, y = map(float, sys.stdin.readline().split())
    stars.append((x, y))

distances = []  # 모든 별 간 거리를 저장하는 힙
for idx1 in range(N):
    x1, y1 = stars[idx1]
    for idx2 in range(idx1 + 1, N):
        x2, y2 = stars[idx2]
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        heapq.heappush(distances, (distance, idx1, idx2))

parents = list(range(N))  # 각 별의 조상 기록
left_stars = N - 1  # 아직 별자리에 포함되지 않은 별의 수
total_cost = 0  # 총 비용
while left_stars:
    dist, star1, star2 = heapq.heappop(distances)
    
    # 이미 별자리에 포함된 별은 무시
    if find(star1) == find(star2):
        continue
    
    parents[find(star2)] = find(star1)  # 조상 갱신
    total_cost += dist  # 비용 추가
    left_stars -= 1  # 별자리에 포함되지 않은 별의 수 감소
print(total_cost)