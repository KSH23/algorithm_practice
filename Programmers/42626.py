# 42626. 더 맵게


import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)  # 리스트를 힙으로 변환
    
    # 가장 낮은 스코빌 지수가 K 이상이 될 때까지 반복
    while scoville[0] < K:
        # 만약 섞을 수 있는 음식이 없다면 실패
        if len(scoville) < 2:
            return -1
        
        # 두 개의 음식을 꺼낸 뒤 합쳐서 다시 추가하고 횟수 증가
        food1, food2 = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, food1 + food2 * 2)
        answer += 1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))