# 4012. 요리사


def calc_synergy(dish1):
    dish2 = set(range(N)) - dish1  # 두번째 요리

    synergy1 = 0  # 첫번째 요리의 시너지
    for i in list(dish1):
        for j in list(dish1):
            if i == j:
                continue
            synergy1 += TABLE[i][j]

    synergy2 = 0  # 두번째 요리의 시너지
    for i in list(dish2):
        for j in list(dish2):
            if i == j:
                continue
            synergy2 += TABLE[i][j]

    return abs(synergy1 - synergy2)


def cook(dish, now, cnt):
    global ans

    if cnt == N // 2:  # 재료 선정 완료
        ans = min(ans, calc_synergy(dish))
        return

    for ingredient in range(now + 1, N):
        dish.add(ingredient)  # 재료 선택
        cook(dish, ingredient, cnt + 1)
        dish.remove(ingredient)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    TABLE = [list(map(int, input().split())) for _ in range(N)]
    ans = 20000 * N  # 최종 정답
    cook(set(), -1, 0)
    print(f'#{tc} {ans}')