# 4880. 토너먼트 카드게임


def rcp(i, j):
    if game_list[i] == 1 and game_list[j] == 3:
        return i
    elif game_list[i] == 3 and game_list[j] == 1:
        return j
    elif game_list[i] < game_list[j]:
        return j
    elif game_list[i] > game_list[j]:
        return i
    else:
        return i


def dfs(i, j):
    if j - i == 1:
        return rcp(i, j)

    if i == j:
        return i

    else:
        return rcp(dfs(i, (i+j) // 2), dfs((i+j) // 2 + 1, j))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 1은 가위 2는 바위 3은 보
    # 1은 3을 이김
    # 2는 1을 이김
    # 3은 2를 이김
    game_list = list(map(int, input().split()))
    print('#{} {}'.format(tc, dfs(0, N-1) + 1))


