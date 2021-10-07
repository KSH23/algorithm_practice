# 1486. 장훈이의 높은 선반


def make_tower(total, now):
    global ans

    if ans < total - B:
        return

    if now == N:
        if 0 <= total - B < ans:
            ans = total - B
        return

    make_tower(total, now + 1)  # 현재 직원 뺌
    make_tower(total + heights[now], now + 1)  # 현재 직원 추가


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    ans = B  # 최종 정답
    make_tower(0, 0)
    print(f'#{tc} {ans}')