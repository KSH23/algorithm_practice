# 5248. 그룹 나누기


def find(x):
    if parents[x] == x:
        return x

    p_x = find(parents[x])
    parents[x] = p_x
    return p_x


def union(x, y):
    p_x = find(x)
    p_y = find(y)

    if group[p_y]:
        parents[p_x] = p_y
        group[p_x] = 0
    else:
        parents[p_y] = p_x
        group[p_y] = 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    parents = list(range(N + 1))
    group = [0] + [1] * N
    partners = list(map(int, input().split()))
    for idx in range(M):
        union(partners[idx * 2], partners[idx * 2 + 1])

    print(f'#{tc} {sum(group)}')