# 7465. 창용 마을 무리의 개수


def find(x):  # 조상 찾기
    if parents[x] == x:
        return x

    p_x = find(parents[x])
    parents[x] = p_x
    return p_x


def union(x, y):  # 조상 합치기
    global group_cnt

    p_x = find(x)
    p_y = find(y)

    if p_x == p_y:
        return

    # 조상이 서로 다르면 조상을 합치고 조상 수를 줄임
    parents[p_y] = p_x
    group_cnt -= 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    parents = [0] + list(range(1, N + 1))
    group_cnt = N
    for _ in range(M):
        person1, person2 = map(int, input().split())
        union(person1, person2)
    print(f'#{tc} {group_cnt}')