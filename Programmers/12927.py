# 12927. 야근 지수


import heapq


def solution(n, works):
    answer = 0

    max_heap = []  # 작업량을 최대순으로 저장
    for work in works:
        answer += work * work
        heapq.heappush(max_heap, -work)

    for _ in range(n):
        if not max_heap:
            break
        
        # 최대 작업량을 1만큼 처리
        number = heapq.heappop(max_heap)
        answer -= number * number
        number += 1
        
        # 작업량이 남은 경우 야근 피로도와 최대힙 갱신
        if number:
            answer += number * number
            heapq.heappush(max_heap, number)

    return answer
