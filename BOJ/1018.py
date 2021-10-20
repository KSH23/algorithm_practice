def check(row, col):
    # 흰색으로 시작한 체스판의 경우
    cnt1 = 0
    # 짝수 row가 check1과 일치하는지, 홀수 row가 check2와 일치하는지 검사
    for i in range(0, 8, 2):
        idx = 0
        while idx < 8:
            if MAP[row + i][col + idx] != check1[idx]:
                cnt1 += 1
            if MAP[row + i + 1][col + idx] != check2[idx]:
                cnt1 += 1
            idx += 1

    # 검은색으로 시작한 체스판의 경우
    cnt2 = 0
    # 짝수 row가 check2과 일치하는지, 홀수 row가 check1와 일치하는지 검사
    for i in range(0, 8, 2):
        idx = 0
        while idx < 8:
            if MAP[row + i][col + idx] != check2[idx]:
                cnt2 += 1
            if MAP[row + i + 1][col + idx] != check1[idx]:
                cnt2 += 1
            idx += 1

    return min(cnt1, cnt2)


R, C = map(int, input().split())
MAP = [input() for _ in range(R)]

check1 = 'WBWBWBWB'
check2 = 'BWBWBWBW'

ans = R * C  # 최종 정답
for r in range(0, R - 8 + 1):
    for c in range(0, C - 8 + 1):
        ans = min(ans, check(r, c))
print(ans)