# 12652. 후위 표기법


T = int(input())
for tc in range(1, T+1):
    isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
    equation = input().rstrip()
    stack = []
    ans = []

    for token in equation:
        if token == ')':
            while stack[-1] != '(':
                temp = stack.pop()
                ans.append(temp)
            stack.pop()
            continue

        if token not in icp:
            ans.append(token)
            continue

        if token == '(':
            stack.append(token)
            continue

        if len(stack) == 0 or icp[token] > isp[stack[-1]]:
            stack.append(token)

        else:
            while len(stack) > 0 and icp[token] <= isp[stack[-1]]:
                temp = stack.pop()
                ans.append(temp)
            stack.append(token)

    while len(stack) > 0:
        temp = stack.pop()
        ans.append(temp)

    ans = ''.join(ans)
    print('#{} {}'.format(tc, ans))





