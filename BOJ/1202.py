# 1202. 보석 도둑


import sys
import heapq


N, K = map(int, sys.stdin.readline().split())

# 보석을 리스트에 저장한 뒤 무게를 기준으로 오름차순 정렬
jewellery = []
for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    jewellery.append((M, V))
jewellery.sort()

# 가방 무게를 리스트에 저장한 뒤 무게를 기준으로 오름차순 정렬
bags = []
for _ in range(K):
    C = int(sys.stdin.readline())
    bags.append(C)
bags.sort()

ans = 0  # 최종 정답
possible_jewellery = []  # 훔칠 수 있는 보석 저장 리스트
j_idx = 0  # 보석 리스트 인덱스
for bag in bags:
    # 각 가방에 대하여 훔칠 수 있는 보석을 리스트에 갱신
    # 이때 최대힙을 이용하여 가치를 기준으로 정렬
    while j_idx < N and jewellery[j_idx][0] <= bag:
        heapq.heappush(possible_jewellery, -jewellery[j_idx][1])
        j_idx += 1

    # 현재 가방에 훔칠 수 있는 보석중 가장 가치가 높은 보석 pop
    if possible_jewellery:
        ans -= heapq.heappop(possible_jewellery)
print(ans)