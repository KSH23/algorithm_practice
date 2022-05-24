# 42628. 이중우선순위큐


import heapq


def solution(operations):
    # 내림차순, 오름차순으로 정렬할 힙과 삭제된 숫자의 인덱스 저장 세트 설정
    max_heap, min_heap = [], []
    deleted_index = set()

    def delete_number(heap_list):
        # 삭제된 인덱스 세트에 포함된 인덱스가 힙에 존재한다면 힙에서 제거
        while heap_list and heap_list[0][1] in deleted_index:
            heapq.heappop(heap_list)

    for index, operation in enumerate(operations):
        command, number = operation.split()
        number = int(number)
        if command == "I":
            heapq.heappush(max_heap, (-number, index))
            heapq.heappush(min_heap, (number, index))
        else:
            # 최대힙과 최소힙에서 이미 삭제된 숫자를 인덱스를 이용해 제거하고
            # 그 결과에서 한번 더 숫자를 제거
            if number == 1 and max_heap:
                delete_number(max_heap)
                if max_heap:
                    deleted_index.add(heapq.heappop(max_heap)[1])
            elif min_heap:
                delete_number(min_heap)
                if min_heap:
                    deleted_index.add(heapq.heappop(min_heap)[1])

    if max_heap and min_heap:
        # 삭제되지 않은 숫자가 있을 경우 이를 제거하고 최댓값과 최솟값 반환
        delete_number(max_heap)
        delete_number(min_heap)

        return [-heapq.heappop(max_heap)[0], heapq.heappop(min_heap)[0]]

    return [0, 0]
