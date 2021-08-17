# 5432. 쇠막대기 자르기


def cutting(li):
    total = 0
    stick = 0

    for i in range(len(li)):
        if li[i] == '(':
            stick += 1
        elif li[i] == ')':
            if li[i - 1] == '(':
                stick -= 1
                total += stick
            else:
                stick -= 1
                total += 1

    return total


T = int(input())
for tc in range(1, T + 1):
    my_li = input()
    print('#{} {}'.format(tc, cutting(my_li)))