# 2819. 격자판의 숫자 이어 붙이기


def go(row, col, cnt, num):
    global ans

    if cnt == 7:  # 숫자 완정
        if num not in num_set:
            ans += 1
            num_set.add(num)
        return

    for d in range(4):
        nr, nc = row + dr[d], col + dc[d]
        if nr < 0 or nc < 0 or 4 <= nr or 4 <= nc:
            continue
        go(nr, nc, cnt + 1, num + MAP[nr][nc])


T = int(input())
for tc in range(1, T + 1):
    MAP = [list(input().split()) for _ in range(4)]
    num_set = set()  # 가능한 숫자를 저장하는 set

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    ans = 0  # 최종 정답
    for r in range(4):
        for c in range(4):
            go(r, c, 0, '')

    print(f'#{tc} {ans}')