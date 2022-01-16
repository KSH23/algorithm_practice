# 2623. 음악프로그램


import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]  # 가수 순서 기록
in_degree = [0] * (N + 1)  # 가수 진입 차수 기록
for _ in range(M):
    singers = list(map(int, sys.stdin.readline().split()))
    for idx in range(1, singers[0]):
        # 뒤에 있는 가수를 graph에 기록하고 그의 진입 차수 증가
        graph[singers[idx]].append(singers[idx + 1])
        in_degree[singers[idx + 1]] += 1

q = deque()
for idx in range(1, N + 1):
    # 진입 차수가 0인 인덱스를 큐에 추가
    if not in_degree[idx]:
        q.append(idx)

ans = []  # 최종 정답
while q:
    singer = q.popleft()
    ans.append(singer)
    
    for next_singer in graph[singer]:
        # 다음 올 수 있는 가수의 진입 차수 감소
        in_degree[next_singer] -= 1
        
        # 진입 차수가 0이 된 가수를 큐에 추가
        if not in_degree[next_singer]:
            q.append(next_singer)

# 모든 가수를 탐색한 경우 이를 출력하고 그렇지 않다면 0 출력
if len(ans) == N:
    print('\n'.join(map(str, ans)))
else:
    print(0)