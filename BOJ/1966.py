# 1966. 프린터 큐


T = int(input())
for _ in range(T):
    N, idx = map(int, input().split())
    priority = list(map(int, input().split()))    # 중요도
    idx_q = list(range(N))    # 인덱스를 담은 큐
    cnt = 0    # 인쇄될 때마다 추가될 변수

    while len(idx_q) > 0:
        now = idx_q.pop(0)    # 인덱스 리스트의 첫번째 원소를 가져온다
        flag = 0

        # 남은 인덱스 리스트의 원소들과 연결된 중요도를 가져와 비교
        # 더 큰 중요도를 가진 인덱스를 만나면 인덱스 리스트 끝으로 append
        for i in idx_q:
            if priority[i] > priority[now]:
                idx_q.append(now)
                break
            else:
                flag += 1    # 더 중요한 인덱스를 만나지 않으면 flag에 1을 추가

        # 만약 flag와 남아있던 인덱스 리스트의 길이가 같다면
        # 현재 원소가 가장 중요한 것이므로 출력하고 cnt에 1 추가
        if flag == len(idx_q):
            cnt += 1
            if now == idx:    # 만약 출력된 인덱스가 내가 찾던 리스트라면 break
                break

    print(cnt)