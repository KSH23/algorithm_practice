# 9935. 문자열 폭발


def bomb(string, target):
    stack = []
    for j in range(len(string)):
        stack.append(string[j])

        if string[j] == target[-1] and len(stack) >= len(target):
            cnt = 0
            for i in range(len(target)):
                if stack[-1 -i] == target[-1 -i]:
                    cnt += 1
            if cnt == len(target):
                for k in range(len(target)):
                    stack.pop()

    if len(stack) == 0:
        return 'FRULA'
    else:
        return stack


my_string = input()
my_target = input()
print(''.join(bomb(my_string, my_target)))