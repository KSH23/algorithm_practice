# 1954. 달팽이 숫자


def snail_list(n):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    cnt = 1
    k = 0
    i, j = 0, -1
    result = [[0] * n for _ in range(n)]

    while cnt <= n**2:
        if n <= i + di[k] or n <= j + dj[k] or i + di[k] < 0 or j + dj[k] < 0:
            k = (k + 1) % 4
        elif result[i + di[k]][j + dj[k]] != 0:
            k = (k + 1) % 4
        else:
            i, j = i + di[k], j + dj[k]
            result[i][j] = cnt
            cnt += 1

    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = snail_list(N)
    print('#{}'.format(tc))
    for i in range(N):
        print('{}'.format(' '.join(map(str, ans[i]))))