# 2606. 바이러스


def dfs(c):
    for i in range(V):
        if MAP[c][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)


V = int(input())
E = int(input())
MAP = [[0] * V for _ in range(V)]

for i in range(E):
    a, b = map(int, input().split())
    MAP[a-1][b-1] = MAP[b-1][a-1] = 1

visited = [0] * V
visited[0] = 1    # 1번 컴퓨터 즉 0번 원소는 이미 방문한 것으로 설정
dfs(0)    # 1번 컴퓨터 즉 0번 원소부터 dfs 시작

ans = 0
for i in range(V):
    if visited[i] == 1:
        ans += 1

# 1번 컴퓨터는 제외하고 수를 셈
print(ans - 1)