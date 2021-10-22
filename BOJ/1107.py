# 1107. 리모컨


import sys
import heapq


def find_channel():
    hq = []  # heapq
    # heapq에 추가할 값: (누른 횟수, 현재 채널, 숫자를 누를 수 있는지)
    heapq.heappush(hq, (0, 100, 0))

    for num in possible_nums:  # 초기값 설정
        heapq.heappush(hq, (1, num, 1))  # 계속 숫자를 누를 수 있으면 1
        heapq.heappush(hq, (1, num, 0))  # 숫자를 누를 수 없으면 0

    while hq:
        push_cnt, cur_num, add_num = heapq.heappop(hq)

        if cur_num == target:  # 초기값 중 목표 채널이 있는 경우
            return push_cnt

        if channels[cur_num][add_num] > -1:  # 이미 계산되었다면
            continue
        channels[cur_num][add_num] = push_cnt

        # 계속 숫자를 누를 수 있는 경우
        if add_num:
            for num in possible_nums:
                new_num = cur_num * 10 + num
                if new_num == target:  # 목표 도달
                    return push_cnt + 1
                if 1000000 < new_num:
                    continue  # 채널 경계를 벗어나는 경우
                heapq.heappush(hq, (push_cnt + 1, new_num, 1))  # 계속 숫자 누를 수 있도록
                heapq.heappush(hq, (push_cnt + 1, new_num, 0))  # 더이상 숫자 누를 수 없도록
        else:
            for delta in [-1, 1]:
                new_num = cur_num + delta
                if new_num == target:  # 목표 도달
                    return push_cnt + 1
                if new_num < 0 or 1000000 < new_num:
                    continue  # 채널 경계를 벗어나는 경우
                heapq.heappush(hq, (push_cnt + 1, new_num, 0))  # 더이상 숫자 누를 수 없도록


target = int(sys.stdin.readline())
broken_cnt = int(sys.stdin.readline())
broken_nums = set()
if broken_cnt > 0:
    broken_nums = set(map(int, sys.stdin.readline().split()))
possible_nums = set(range(10)) - broken_nums  # 누를 수 있는 숫자

channels = [[-1, -1] for _ in range(1000001)]  # 몇 번 눌러야 인덱스 번호 채널에 갈 수 있는지
print(find_channel())