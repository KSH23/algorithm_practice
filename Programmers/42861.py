# 42861. 섬 연결하기


def find(node, parents):
    # 노드의 부모를 구하고, 저장한 뒤 반환
    if parents[node] == node:
        return node

    parent = find(parents[node], parents)
    parents[node] = parent

    return parent


def solution(n, costs):
    costs.sort(key=lambda item: item[2])  # 비용을 기준으로 정렬
    parents = [index for index in range(n)]  # 각 노드의 부모 노드 저장
    total_cost = 0  # 총 비용

    for node1, node2, cost in costs:
        node1_parent, node2_parent = find(node1, parents), find(node2, parents)
        if node1_parent != node2_parent:  # 사이클이 아닌 경우
            parents[node1_parent] = node2_parent  # 부모 갱신
            total_cost += cost  # 비용 갱신

    return total_cost
