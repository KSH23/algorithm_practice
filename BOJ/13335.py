# 13335. 트럭


n, w, L = map(int, input().split())  # 트럭의 수, 다리의 길이, 최대 하중
trucks = list(map(int, input().split()))
t_idx = 0  # 현재 대기중인 트럭의 인덱스
on_bridge = 0   # 현재 다이 위에 놓인 트럭의 하중
trucks_time = [0] * n  # 각 트럭이 다리를 탈출하기 위해 걸리는 시간
left_truck = 0  # 가장 먼저 들어간 트럭의 인덱스
t = 1  # 소요 시간
while left_truck < n:
    # 다리에 트럭을 올릴 수 있는 경우
    if t_idx < n and on_bridge + trucks[t_idx] <= L:
        on_bridge += trucks[t_idx]
        trucks_time[t_idx] = w + t - 1
        t_idx += 1

    # 가장 먼저 들어간 트럭이 다리를 통과할 수 있는 경우
    if trucks_time[left_truck] == t:
        on_bridge -= trucks[left_truck]
        left_truck += 1

    t += 1
print(t)