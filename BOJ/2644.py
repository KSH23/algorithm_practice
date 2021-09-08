# 2644. 촌수계산


def dfs(now):
    if now == end:
        return

    for i in range(1, n+1):
        if MAP[now][i] == 1 and visited[i] == -1:
            visited[i] = visited[now] + 1
            dfs(i)


n = int(input())    # 전체 사람의 수
start, end = map(int, input().split())
m = int(input())    # 간선 수

MAP = [[0] * (n + 1) for _ in range(n + 1)]    # 친족 리스트
visited = [-1] * (n + 1)    # 최단 경로 저장 리스트
visited[start] = 0

for _ in range(m):    # 친족 관계 맵 형성
    p, c = map(int, input().split())
    MAP[p][c] = 1
    MAP[c][p] = 1

dfs(start)
print((visited[end]))