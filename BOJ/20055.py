# 20055. 컨베이어 벨트 위의 로봇


N, K = map(int, input().split())
conveyor = list(map(int, input().split()))

k_cnt = 0  # 내구도가 0인 칸의 개수
up, down = 0, N - 1  # 올리는 위치와 내리는 위치의 인덱스

robots = [0] * 2 * N  # [인덱스]칸에 로봇 존재 유무 표시

step = 0  # 총 단계 수

while k_cnt < K:
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
    up = (up + 2 * N - 1) % (2 * N)
    down = (down + 2 * N - 1) % (2 * N)
    robots[down] = 0  # 내리는 위치의 로봇은 내림

    # 2. 로봇 이동
    for idx in range(down, down - N, -1):  # 가장 먼저 올라간 로봇부터
        if robots[idx] == 0:  # idx 위치에 로봇이 없으면 넘어감
            continue
        next_idx = (idx + 1) % (2 * N)  # 회전하는 방향의 다음 칸
        if robots[next_idx] == 0 and conveyor[next_idx] > 0:
            robots[next_idx] = 1  # 한 칸 전진
            conveyor[next_idx] -= 1  # 컨베이어 벨트 내구도 하락
            if conveyor[next_idx] == 0:
                k_cnt += 1  # 내구도가 0이 된 경우
            robots[idx] = 0  # 기존 칸은 비워줌
    robots[down] = 0  # 내리는 위치의 로봇은 내림

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올림
    if conveyor[up]:
        robots[up] = 1
        conveyor[up] -= 1  # 컨베이어 벨트 내구도 하락
        if conveyor[up] == 0:
            k_cnt += 1  # 내구도가 0이 된 경우

    step += 1

print(step)