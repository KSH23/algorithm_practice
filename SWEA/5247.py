# 5247. 연산


from collections import deque


def bfs(num):
    if num == M:
        return 0
    q = deque()
    q.append(num)
    while q:
        now = q.popleft()
        for operator in [1, -1, now, -10]:
            next_num = now + operator
            if next_num > 1000000 or next_num < 1:
                continue
            if visited[next_num] > -1:
                continue
            visited[next_num] = visited[now] + 1
            if next_num == M:
                return visited[next_num]
            q.append(next_num)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [-1] * 10000001
    visited[N] = 0
    ans = 10000000
    print(f'#{tc} {bfs(N)}')