# 2005. 파스칼의 삼각형


def tri(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        pre = tri(n-1)
        li = [1]
        for i in range(len(pre) - 1):
            li.append(pre[i] + pre[i+1])
        li.append(1)
        return li


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    print('#{}'.format(tc))
    for i in range(N):
        print(' '.join(map(str, tri(i))))