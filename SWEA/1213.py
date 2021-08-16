# 1213. String


def count_str(target, string):
    cnt = 0
    x = 0
    while x <= len(string) - len(target):
        if string[x] == target[0]:
            for i in range(len(target)):
                if string[x] != target[i]:
                    break
                if i == len(target) - 1:
                    cnt += 1
                x += 1
        else:
            x += 1

    return cnt


T = 10
for tc in range(1, 1+T):
    test_number = int(input())
    target_str = input()
    my_string = input()
    print('#{} {}'.format(tc, count_str(target_str, my_string)))