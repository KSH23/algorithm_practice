# 1068. 트리


def dfs(now):
    global ans

    if now == del_node:  # 만약 현재 노드가 삭제할 노드라면
        return 1  # 1을 반환

    if not tree[now]:  # 자식 노드가 없는 경우
        ans += 1
        return

    del_cnt = 0  # 이번 노드의 자식이 삭제된 경우를 표시
    for i in range(len(tree[now])):
        if dfs(tree[now][i]):
            del_cnt += 1

    # 현재 노드 아래 자손이 없어져 노드가 리프로 바뀌는 경우
    if del_cnt == len(tree[now]):
        ans += 1


N = int(input())
temp_list = list(map(int, input().split()))  # 입력값을 받는 임시 리스트
tree = [[] for _ in range(N)]  # tree[노드] = [자식노드 리스트]
root = 0  # 루트
for idx in range(N):  # tree 리스트 형성 + 루트 찾기
    if temp_list[idx] == -1:
        root = idx
        continue
    tree[temp_list[idx]].append(idx)

del_node = int(input())  # 삭제할 노드
ans = 0  # 최종 정답
dfs(root)
print(ans)