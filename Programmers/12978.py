# 12978. 배달


from collections import deque


def solution(N, road, K):
    answer = 1

    # 각 마을에서 갈 수 있는 마을을 시간과 함께 기록하는 배열
    edges = [[] for _ in range(N)]
    for a, b, time in road:
        edges[a - 1].append((b - 1, time))
        edges[b - 1].append((a - 1, time))

    # 마을의 방문 여부를 도달한 시간으로 기록하는 배열
    visited = [-1] * N
    visited[0] = 0  # 시작 마을

    dq = deque([(0, 0)])
    while dq:
        current_city, time = dq.popleft()  # 현재 도착한 마을, 걸린 시간

        for next_city, next_time in edges[current_city]:
            if K < time + next_time:  # 시간이 초과되는 경우
                continue
            if -1 < visited[next_city] < next_time + time:  # 더 짧은 시간 안에 도달했던 경우
                continue

            if visited[next_city] == -1:  # 처음 방문하는 경우 답 증가
                answer += 1
            visited[next_city] = next_time + time  # 방문 표시
            dq.append((next_city, time + next_time))

    return answer
