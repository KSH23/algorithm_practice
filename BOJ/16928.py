# 16928. 뱀과 사다리 게임


import sys
from collections import deque


def move():
    q = deque()
    q.append(1)

    while q:
        current_step = q.popleft()

        for dice in range(1, 7):
            next_step = current_step + dice

            # 뱀 또는 사다리가 존재하는 경우 갈 수 있는데까지 계속 이동
            while move_dict.get(next_step):
                next_step = move_dict[next_step]

            if next_step > 100:  # 칸을 벗어나는 경우
                continue

            if -1 < visited[next_step]:  # 이미 방문한 경우
                continue

            visited[next_step] = visited[current_step] + 1
            q.append(next_step)


N, M = map(int, sys.stdin.readline().split())
move_dict = {}  # 뱀과 사다리 위치와 목적지를 저장
for _ in range(N + M):
    start, end = map(int, sys.stdin.readline().split())
    move_dict[start] = end

visited = [-1] * 101  # 방문 표시
visited[1] = 0  # 초기 위치
move()
print(visited[100])