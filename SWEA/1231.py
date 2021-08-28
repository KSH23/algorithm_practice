# 1231. 중위순회


def postorder_traverse(t):
    if G[2*t] != 0:
        postorder_traverse(G[2*t])

    ans.append(t)

    if G[2*t + 1] != 0:
        postorder_traverse(G[2*t+1])


for tc in range(1, 11):
    V = int(input())
    G = [0] * (2 * (V + 1))
    LETTER = [0] * (V+1)
    for i in range(V):
        data = list(input().split())

        for i in range(len(data)):
            if i == 1:
                continue
            data[i] = int(data[i])

        LETTER[data[0]] = data[1]
        if len(data) == 4:
            G[data[0] * 2] = data[2]
            G[data[0] * 2 + 1] = data[3]
        elif len(data) == 3:
            G[data[0] * 2] = data[2]

    ans = []
    postorder_traverse(1)
    word_ans = ''

    for i in range(len(ans)):
        word_ans += LETTER[ans[i]]

    print('#{} {}'.format(tc, word_ans))
