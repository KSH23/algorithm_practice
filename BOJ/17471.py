# 17471. 게리맨더링


import sys
from collections import deque


def validate(initial_set):
    d_set = initial_set.copy()  # set 복사
    q = deque()  # deque 생성
    q.append(d_set.pop())
    while len(d_set) and q:  # BFS 실행
        now = q.popleft()
        for d in list(d_set):
            if MAP[now][d]:
                q.append(d)
                d_set.remove(d)

    if len(d_set):  # 선거구를 모두 가지 못한 경우
        return False
    return True


def divide(now, district1):
    global ans

    if now == N + 1:  # 모든 선거구를 확인한 경우
        if 0 < len(district1) < N:
            district2 = set(range(1, N + 1)) - district1
            if validate(district1) and validate(district2):
                p1 = sum([population[idx] for idx in list(district1)])
                p2 = sum([population[idx] for idx in list(district2)])
                ans = min(ans, abs(p1 - p2))
        return

    divide(now + 1, district1)  # now 선거구를 택하지 않은 경우
    district1.add(now)
    divide(now + 1, district1)  # now 선거구를 택한 경우
    district1.remove(now)


N = int(input())
population = [0] + list(map(int, sys.stdin.readline().split()))
MAP = [[0] * (N + 1) for _ in range(N + 1)]  # 선거구 연결 리스트
for district in range(1, N + 1):
    temp = list(map(int, sys.stdin.readline().split()))
    for i in range(temp[0]):
        MAP[district][temp[i + 1]] = 1
        MAP[temp[i + 1]][district] = 1

ans = 1000
divide(1, set())
if ans == 1000:  # 선거구를 정할 수 없는 경우
    print(-1)
else:
    print(ans)