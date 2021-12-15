# 86971. 전력망을 둘로 나누기


def find(x, parents):
    # 조상 찾은 후 조상 값 반환
    if parents[x] == x:
        return x
    px = find(parents[x], parents)
    parents[x] = px
    return px


def solution(n, wires):
    answer = n

    # 제거할 간선을 선택 후 탐색
    for deleted_wire in range(n - 1):
        parents = list(range(n + 1))  # 조상 저장 배열

        # 제거된 간선을 제외하고 모든 간선에 대해 조상 결합 작업 진행
        for wire_idx in range(n - 1):
            if wire_idx == deleted_wire:
                continue
            v1, v2 = wires[wire_idx]
            pv1, pv2 = find(v1, parents), find(v2, parents)
            if pv1 != pv2:
                parents[pv2] = pv1

        # 두 개로 좁혀진 조상을 key, 같은 조상을 같는 정점의 수를 value로 딕셔너리에 저장
        parents_dict = dict()
        for p in parents[1:]:
            parent = find(p, parents)
            if parent in parents_dict:
                parents_dict[parent] += 1
            else:
                parents_dict[parent] = 1

        # 최솟값 갱신
        answer = min(answer, abs(list(parents_dict.values())[0] - list(parents_dict.values())[1]))

    return answer