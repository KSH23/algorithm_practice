# 1043. 거짓말


import sys


def find(x):
    if parents[x] == x:
        return x
    parent_x = find(parents[x])
    parents[x] = parent_x
    return parent_x  # 조상 반환


N, M = map(int, sys.stdin.readline().split())
truth = list(map(int, sys.stdin.readline().split()))
avoid_people = set()  # 피해야 하는 사람들

parents = list(range(N + 1))  # 조상 리스트

# 피해야 하는 사람은 set에 추가하고 조상을 0으로 기록
if 1 < len(truth):
    for person in truth[1:]:
        avoid_people.add(person)
        parents[person] = 0

possible_party = []  # 일단 갈 수 있는 파티 목록
for _ in range(M):
    party = list(map(int, sys.stdin.readline().split()))
    standard_person = party[1]  # 기준으로 잡을 사람
    if 1 < party[0]:  # 2명 이상 있는 경우
        # 각 사람에 대하여 기준 사람과 비교해 최솟값 조상으로 갱신
        for person in party[2:]:
            parent_s_person = find(standard_person)
            parent_person = find(person)
            parents[parent_s_person] = min(parent_s_person, parent_person)
            parents[parent_person] = min(parent_s_person, parent_person)

    # 기준으로 잡은 사람의 조상이 0이 아니면 일단 갈 수 있는 파티에 추가
    if parents[standard_person]:
        possible_party.append(party)

ans = len(possible_party)

# 갈 수 있는 파티를 돌며 조상이 0인 사람을 만나면 갯수 감소
for party in possible_party:
    for person in party[1:]:
        if find(person) == 0:
            ans -= 1
            break
print(ans)