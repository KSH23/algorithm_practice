# 7662. 이중 우선순위 큐


import sys
import heapq


T = int(sys.stdin.readline())
for tc in range(T):
    N = int(sys.stdin.readline())  # 연산의 개수
    min_heap = []  # 최소 힙
    max_heap = []  # 최대 힙
    links = [0] * N  # i번째 들어온 원소의 존재 유무 표시
    pop_cnt = 0  # 추가 횟수 - 삭제 횟수, 마지막에 음수가 되면 큐가 비어있는 것
    for i in range(N):
        command, str_num = sys.stdin.readline().split()
        int_num = int(str_num)
        if command == 'I':
            pop_cnt += 1
            links[i] = 1  # 원소 존재 표시
            heapq.heappush(min_heap, (int_num, i))
            heapq.heappush(max_heap, (-1 * int_num, i))
        else:
            if pop_cnt > 0:  # 큐가 채워져 있을 때에만 1 감소
                pop_cnt -= 1
            if int_num == 1:  # pop max heap
                if max_heap:  # 원소가 있을 경우에만
                    pop_num, order = heapq.heappop(max_heap)
                    if links[order] == 0:  # 이미 삭제된 원소인 경우
                        while links[order] == 0 and max_heap:  # 이후의 삭제된 원소 지우기
                            pop_num, order = heapq.heappop(max_heap)
                    links[order] = 0
            else:  # pop min heap
                if min_heap:  # 원소가 있을 경우에만
                    pop_num, order = heapq.heappop(min_heap)
                    if links[order] == 0:  # 이미 삭제된 원소인 경우
                        while links[order] == 0 and min_heap:  # 이후의 삭제된 원소 지우기
                            pop_num, order = heapq.heappop(min_heap)
                    links[order] = 0

    if pop_cnt <= 0:  # 비어있는 경우
        print('EMPTY')
    else:
        min_value, order = heapq.heappop(min_heap)
        while links[order] == 0:  # 삭제되지 않은 숫자 찾기
            min_value, order = heapq.heappop(min_heap)

        max_value, order = heapq.heappop(max_heap)
        while links[order] == 0:  # 삭제되지 않은 숫자 찾기
            max_value, order = heapq.heappop(max_heap)
        print(-1 * max_value, min_value)