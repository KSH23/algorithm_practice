# 1389. 케빈 베이컨의 6단계 법칙


N, M = map(int, input().split())
MAP = [[] for _ in range(N + 1)]

for _ in range(M):    # 친구 맵 생성
    A, B = map(int, input().split())
    MAP[A].append(B)
    MAP[B].append(A)

min_bacon = N ** 2    # 최소 베이컨 수
popular_person = 0    # 가장 베이컨이 적은 사람

for person in range(1, N + 1):    # 모든 사람에 대해 검사
    visited = [0] * (N + 1)    # 검사한 친구 목록
    total_bacon = 0    # 현재 베이컨 수
    q = [person]    # 큐 생성
    visited[person] = 1    # 본인 체크
    while len(q) > 0:    # BFS 실행
        now = q.pop(0)
        for friend in list(MAP[now]):
            if visited[friend]:
                continue
            q.append(friend)
            visited[friend] = visited[now] + 1
            total_bacon += visited[now]    # 베이컨 수 갱신
    if total_bacon < min_bacon:    # 최소 베이컨 갱신
        popular_person = person
        min_bacon = total_bacon

print(popular_person)