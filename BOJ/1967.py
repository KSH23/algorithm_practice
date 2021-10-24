# 1967. 트리의 지름


import sys


sys.setrecursionlimit(100000)


def dfs(cur_node, total_cost):
    global ans

    max_ret = 0  # cur_node의 가지의 가충치를 모두 합했을 때 그중 가장 큰 값
    for node, cost in tree[cur_node]:
        if visited[node]:
            continue  # 이미 방문한 노드 무시

        visited[node] = True  # 방문 표시

        # cur_node에서 node로 시작되는 가지의 가중치 총 합
        ret = dfs(node, total_cost + cost) + cost

        # cur_node는 자신의 가지 중 2개를 선택해 지름을 구성해야 함
        # 지름의 최댓값을 구해야하므로 가장 큰 ret 값과 두번째로 큰 ret 값을 더해야 함
        # 구한 ret 값과 max_ret 값을 더한다면 어느 시점에 아래 두 경우가 생길 수 있음
        # case1. total_ret = (ret: 가장 큰 가중치) + (max_ret: 두번째로 큰 가중치)
        # case2. total_ret = (ret: 두번째로 큰 가중치) + (max_ret: 가장 큰 가중치)
        # 따라서 total_ret 값을 계속 갱신하면 어느 시점에 최대 지름을 구할 수 있다
        total_ret = ret + max_ret
        ans = max(ans, total_ret)  # 최종 답에 최댓값 갱신
        max_ret = max(max_ret, ret)  # 최댓값 갱신
        visited[node] = False  # 방문 표시 취소

    costs[cur_node] = max_ret  # (디버깅용) 최대 가중치 저장
    return max_ret


V = int(sys.stdin.readline())

# 연결 관계 생성
tree = [[] for _ in range(V + 1)]
for _ in range(V - 1):
    node1, node2, weight = map(int, sys.stdin.readline().split())
    tree[node1].append([node2, weight])
    tree[node2].append([node1, weight])

visited = [False] * (V + 1)  # 방문 표시 리스트
costs = [-1] * (V + 1)  # (디버깅용) 각 노드의 가지의 가중치 중 가장 큰 값 저장
visited[1] = True  # 항상 존재하는 1번 노드를 기준으로 잡고 먼저 방문 표시
ans = 0  # 최종 답
dfs(1, 0)
print(ans)