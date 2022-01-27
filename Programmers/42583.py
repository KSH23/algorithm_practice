# 42583. 다리를 지나는 트럭


def solution(bridge_length, weight, truck_weights):
    time = 1  # 소요 시간

    bridge = [bridge_length]
    s, e = 0, 1
    total_weight = truck_weights[0]

    while s < e:
        for idx in range(s, e):
            bridge[idx] -= 1

            if bridge[idx] == 0:
                total_weight -= truck_weights[s]
                s += 1

        if e - s < bridge_length and e < len(truck_weights) and total_weight + truck_weights[e] <= weight:
            bridge.append(bridge_length)
            total_weight += truck_weights[e]
            e += 1

        time += 1

    return time