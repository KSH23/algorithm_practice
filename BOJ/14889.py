# 14889. 스타트와 링크


def find_min(t1q):
    global ans

    team1 = 0
    team2 = 0
    t2q = []    # 두번째 팀 목록 생성
    for i in range(N):
        if i in t1q:
            continue
        t2q.append(i)

    for p1 in range(len(t1q)):
        for p2 in range(p1 + 1, len(t1q)):
            team1 += MAP[t1q[p1]][t1q[p2]] + MAP[t1q[p2]][t1q[p1]]

    for p1 in range(len(t2q)):
        for p2 in range(p1 + 1, len(t2q)):
            team2 += MAP[t2q[p1]][t2q[p2]] + MAP[t2q[p2]][t2q[p1]]

    if abs(team1 - team2) < ans:
        ans = abs(team1 - team2)


def make_team(start):
    if len(q) == N // 2:
        find_min(q)
        return

    for i in range(start, N):
        q.append(i)
        make_team(i + 1)
        q.pop()


N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
q = []
ans = 100*400
make_team(0)
print(ans)