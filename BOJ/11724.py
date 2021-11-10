# 11724. 연결 요소의 개수


import sys


def find(x):
    # 조상을 찾아 반환
    if parents[x] == x:
        return x
    p_x = find(parents[x])
    parents[x] = p_x
    return p_x


N, M = map(int, input().split())
parents = list(range(N + 1))  # 조상 저장 리스트

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    u_parent = find(u)
    v_parent = find(v)

    # 각 정점의 조상이 같으면 무시하고 아니면 조상 통일
    if u_parent == v_parent:
        continue
    parents[v_parent] = u_parent

cnt = -1  # 0번 인덱스 값이 0이므로 이를 빼기 위해 -1에서 시작
for idx, parent in enumerate(parents):
    if idx == parent:
        cnt += 1
print(cnt)