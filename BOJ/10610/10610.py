# 10610. 30


def thirty(n):
    total_sum = 0
    for i in range(len(n)):
        total_sum += int(n[i])

    if '0' not in n or total_sum % 3 != 0:
        return -1

    cnt = [0] * 10
    for i in range(len(n)):
        cnt[int(n[i])] += 1

    return cnt


N = input()
result = thirty(N)
if result == -1:
    print(-1)
else:
    for i in range(9, -1, -1):
        for j in range(result[i]):
            print(i, end='')