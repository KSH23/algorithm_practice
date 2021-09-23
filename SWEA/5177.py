# 5177. 이진 힙


import heapq


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    heap = []
    for item in num_list:
        heapq.heappush(heap, item)

    ans = 0
    node_index = len(num_list)
    while True:
        node_index //= 2
        ans += heap[node_index - 1]

        if node_index - 1 == 0:
            break

    print(f'#{tc} {ans}')