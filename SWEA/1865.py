# 1865. 동철이의 일 분배


def distribute(possibility, employee):
    global ans

    # 현재 확률이 저장된 최대 확률보다 작다면 가망 없음
    if possibility <= ans:
        return

    if employee == N:
        if ans < possibility:
            ans = possibility
        return

    for work in range(N):
        if work_check[work]:
            continue
        work_check[work] = employee + 1
        distribute(possibility * MAP[employee][work] / 100, employee + 1)
        work_check[work] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    work_check = [0] * N  # 일한 직원 표시
    ans = 0
    distribute(1, 0)
    print(f'#{tc} {ans * 100:.6f}')