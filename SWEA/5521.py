# 5521. 상원이의 생일파티


def bfs():
    global friends_cnt

    q = [1]
    invited = [0] * (N + 1)  # 초대된 사람 표시
    invited[1] = 1  # 본인은 참석
    cnt = 0
    while q and cnt < 2:  # while loop를 두 번 돌면 친구의 친구까지만 확인됨
        for _ in range(len(q)):
            now = q.pop(0)
            for person in range(2, N + 1):
                if invited[person]:
                    continue
                if MAP[now][person]:
                    invited[person] = 1
                    friends_cnt += 1
                    q.append(person)
        cnt += 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    MAP = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        person1, person2 = map(int, input().split())
        MAP[person2][person1] = 1
        MAP[person1][person2] = 1
    friends_cnt = 0  # 초대할 친구 수
    bfs()

    print(f'#{tc} {friends_cnt}')