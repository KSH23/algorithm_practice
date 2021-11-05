# 1764. 듣보잡


N, M = map(int, input().split())
never_heard = set()  # 듣도 못한 사람 명단
never_seen = set()  # 보도 못한 사람 명단
for _ in range(N):
    never_heard.add(input())
for _ in range(M):
    never_seen.add(input())

# 듣도 보도 못한 사람은 두 set의 합집합
never_heard_and_seen = list(never_heard & never_seen)
never_heard_and_seen.sort()  # 사전순 정렬

print(len(never_heard_and_seen))
for i in range(len(never_heard_and_seen)):
    print(never_heard_and_seen[i])
