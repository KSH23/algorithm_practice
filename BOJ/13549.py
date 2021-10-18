# 13549. 숨바꼭질 3


import heapq


def find():
    if N == K:  # 동생과 같은 위치에 있는 경우
        return 0

    hq = []  # heapq
    heapq.heappush(hq, [0, N])  # 시작 지점 설정
    seconds = [100001] * 100001  # 최소 걸리는 시간 저장
    seconds[N] = 0  # 시작 지점 시간 초기화

    while hq:
        sec, current_pos = heapq.heappop(hq)  # 현재 시간과 위치
        for delta in [-1, 1, current_pos]:
            next_pos = current_pos + delta  # 다음 위치
            if next_pos < 0 or 100000 < next_pos:
                continue  # 경계를 벗어나는 경우
            if seconds[next_pos] != 100001:
                continue  # 이미 방문한 적 있는 경우

            if delta == current_pos:  # 좌, 우로 이동한 경우
                if sec < seconds[next_pos]:  # 더 짧은 시간안에 갈 수 있다면
                    seconds[next_pos] = sec  # 갱신
                    heapq.heappush(hq, [sec, next_pos])
            else:  # 2배를 순간이동한 경우
                if sec + 1 < seconds[next_pos]:  # 더 짧은 시간안에 갈 수 있다면
                    seconds[next_pos] = sec + 1  # 갱신
                    heapq.heappush(hq, [sec + 1, next_pos])

            if next_pos == K:  # 도착
                return seconds[next_pos]


N, K = map(int, input().split())
print(find())