# 2448. 별 찍기 - 11


def make_star(size):
    if size == 3:
        return initial_star

    # 이전 단계의 별
    one_third_star = make_star(size // 2)
    ret = []

    # 상단 별
    for row in one_third_star:
        ret.append([' ' * (size // 2)] + row + [' ' * (size // 2)])

    # 하단 두 개의 별
    for row in one_third_star:
        ret.append(row + [' '] + row)

    return ret


N = int(input())
initial_star = [
    [' ', ' ', '*', ' ', ' '],
    [' ', '*', ' ', '*', ' '],
    ['*', '*', '*', '*', '*']
]
ans = make_star(N)
for r in ans:
    print(''.join(r))