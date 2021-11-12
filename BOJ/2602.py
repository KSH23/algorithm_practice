# 2602. 돌다리 건너기


def dfs(row, now_idx, needed_char_idx):
    if needed_char_idx == len(scroll):  # 원하는 목표에 도착한 경우
        return 1

    # 이미 방문했고 계산한 값이 있다면 이를 반환
    if -1 < now_idx and -1 < dp[row][now_idx][needed_char_idx]:
        return dp[row][now_idx][needed_char_idx]

    result = 0
    next_row = 1 - row  # 다리는 0번과 1번을 왔다갔다 해야 함
    for idx in range(now_idx + 1, len(bridges[0])):
        # 다음 필요한 글자를 만난 경우 그 곳으로 이동
        if bridges[next_row][idx] == scroll[needed_char_idx]:
            result += dfs(next_row, idx, needed_char_idx + 1)

    dp[row][now_idx][needed_char_idx] = result
    return result


scroll = input()
bridges = [list(input()) for _ in range(2)]  # 다리 리스트

# 갈 수 있는 방법의 수를 저장하는 dp
dp = [[[-1] * len(scroll) for _ in range(len(bridges[0]))] for _ in range(2)]

print(dfs(0, -1, 0) + dfs(1, -1, 0))