# 12445. Baby Gin


def find_babygin(num_list):
    li = [0]*10

    for num in num_list:
        li[num] += 1

    i = 0
    count = 0
    while i < 8:
        if li[i] >= 3:
            li[i] -= 3
            count += 1
            continue
        if li[i] >= 1 and li[i+1] >= 1 and li[i+2] >= 1:
            li[i] -= 1
            li[i+1] -= 1
            li[i+2] -= 1
            count += 1
            continue
        i += 1

    if count == 2:
        return 'Baby Gin'
    else:
        return 'Lose'


T = int(input())
for tc in range(1, T+1):
    my_list = list(map(int, ' '.join(input()).split()))
    print('#{} {}'.format(tc, find_babygin(my_list)))