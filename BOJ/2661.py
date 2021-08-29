# 2661. 좋은수열


def dfs(now):
    global stack, ans

    stack += [now]    # 1. 스택에 now를 추가한다

    # 2. 스택이 좋은 수열인지 검사한다
    #    스택의 길이가 3 이하라면 검사할 필요는 없다
    if len(stack) >= 4:
        # 2개씩, 3개씩, ... , 스택의 길이 // 2개씩 묶어 검사를 진행한다
        for i in range(4, len(stack) + 1):
            limit = i // 2
            # 만약 나쁜 수열이 된다면 스택에서 pop을 하고 1을 반환한다
            # 반환되는 1은 이후 fail에 축적된다
            if stack[len(stack) - limit:] == stack[len(stack) - 2 * limit: len(stack) - limit]:
                stack.pop()
                return 1

    # 3. 만약 스택이 좋은 수열 검사를 통과했다면 정답 ans 변수에 추가하고
    #    이후 절대 다시 검사하여 ans를 변경하는 일이 없도록 아무 큰 숫자(100)를 반환한다
    if len(stack) >= N:
        ans = stack
        return 100

    fail = 0    # 총 실패 횟수를 세는 변수

    # 4. 아직 스택의 길이가 부족하다면 새로운 값을 추가하는 과정을 시작한다
    for j in range(1, 4):
        # 5. 숫자 1, 2, 3 중에서 스택의 마지막 값은 무시한다
        if stack[-1] == j:
            continue

        # 6. 스택에 j가 들어가도 되는지 검사하기 위해 다시 dfs 함수에 들어가 2번 과정을 거치며
        #    그 결과를 fail에 저장한다
        fail += dfs(j)

        # 7. 만약 fail이 2라면 스택의 마지막 값과 다른 두 숫자를 넣어서 둘 다 실패했다는 것이므로
        #    스택에서 숫자를 하나 더 빼야 한다
        if fail == 2:
            stack.pop()

        # 만약 3번 과정을 거쳤다면 또 아무 큰 숫자(100)를 반환하여 더 이상 깊게 들어가지 않도록 한다
        if fail >= 100:
            return 100

    return 0


N = int(input())
stack = []
dfs(1)
print(''.join(map(str, ans)))