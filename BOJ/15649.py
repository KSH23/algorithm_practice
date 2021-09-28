# 15649. N과 M(1)


def dfs(num):
    global ans

    ans += [num]    # 순열에 숫자를 넣음
    
    if len(ans) == M:    # 만약 M개의 숫자가 들어가면 끝
        print(' '.join(map(str, ans)))
        return

    for i in range(1, N+1):
        if i in ans:    # 중복된 숫자는 넣지 않음
            continue
        dfs(i)
        ans.pop()


N, M = map(int, input().split())

for x in range(1, N + 1):
    ans = []    # 조건을 만족하는 순열을 담을 리스트
    dfs(x)