# 5202. 화물 도크


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    time_table = [list(map(int, input().split())) for _ in range(N)]
    time_table.sort(key=lambda x: x[1])

    ans = 1
    now = time_table[0]
    for truck in time_table:
        if truck[0] < now[1]:  # 지금 작업 이전에 시작되어야 하는 작업
            continue
        now = truck
        ans += 1

    print(f'#{tc} {ans}')