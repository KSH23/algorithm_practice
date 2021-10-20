# 15971. 두 로봇


import sys


sys.setrecursionlimit(1000000000)


def dfs(current_room, max_length, total_length):
    # max_length: 현재 방까지 오는 과정 중 가장 길었던 길이
    # total_length: 현재 방까지의 총 길이

    global ans

    if current_room == robot2:  # 도착
        ans = min(ans, total_length - max_length)  # 최소 길이 갱신
        return

    for new_room, new_length in cave[current_room]:
        if visited[new_room]:  # 이미 방문했던 방은 무시
            continue
        visited[new_room] = True
        dfs(new_room, max(max_length, new_length), total_length + new_length)
        visited[new_room] = False


N, robot1, robot2 = map(int, sys.stdin.readline().split())
cave = [[] for _ in range(N + 1)]  # 연결 관계 기록
for _ in range(N - 1):
    room1, room2, length = map(int, sys.stdin.readline().split())
    cave[room1].append([room2, length])
    cave[room2].append([room1, length])
visited = [False] * (N + 1)  # 방문 표시
ans = 100000000  # 최종 정답
dfs(robot1, 0, 0)
print(ans)
