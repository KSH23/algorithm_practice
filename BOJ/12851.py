# 12851. 숨바꼭질 2


from collections import deque


def find_sister(start_loc):
    q = deque()
    q.append(start_loc)
    memo[start_loc] = [0, 1]  # 초기 위치 설정

    flag = True  # 동생을 찾으면 False
    while flag:
        for _ in range(len(q)):
            current_loc = q.popleft()
            if current_loc == K:  # 동생을 찾은 경우
                return memo[K]

            for step in [-1, 1, current_loc]:
                # 다음 위치와 걸리는 최단 시간
                next_loc = current_loc + step
                next_time = memo[current_loc][0] + 1
                if next_loc < 0 or 100000 < next_loc:  # 범위 밖
                    continue

                # 이미 최단 시간이 기록된 경우
                if -1 < memo[next_loc][0]:
                    # 최단 시간으로 또 도달한 경우 현재 칸으로 올 수 있는
                    # 방법의 수 만큼 총 방법의 수 증가
                    if next_time == memo[next_loc][0]:
                        memo[next_loc][1] += memo[current_loc][1]
                    continue

                # 처음 방문한 경우 걸린 최단 시간과 방법의 수 저장장
                emo[next_loc] = [next_time, memo[current_loc][1]]
                q.append(current_loc + step)


N, K = map(int, input().split())

# 인덱스 위치로 이동할 수 있는 최단 시간과 방법의 수 기록
memo = [[-1, 0] for _ in range(100001)]

for ans in find_sister(N):
    print(ans)