# 2477. 참외밭


# 방향을 담은 리스트, 면적을 담은 리스트를 인자로 받음
def melon_farm(n, melon_dir, melon_area):
    # 방향 리스트에서 두 번만 등장하는 변의 index을 구함(long _side)
    long_sides = []
    for i in range(1, 5):
        if melon_dir.count(i) == 1:
            long_sides.append(melon_dir.index(i))

    # 각각의 변에서 각각 3칸 떨어진 요소가 없애야 하는 작은 사각형의 변(short_side)
    # 따라서 index에 3을 더한 값을 저장
    short_sides = [x+3 for x in long_sides]

    # 각 숫자를 나타내는 이름이 너무 길어져서 간단하게 바꿔줌
    l1, l2, s1, s2 = long_sides[0], long_sides[1], short_sides[0], short_sides[1]

    # 3칸 떨어진 요소를 구할 때 index out of range가 나올 수 있으므로
    # 면적을 찾을 때 면적 리스트 두 개를 이어붙인 결과에서 찾음
    melon_area = melon_area + melon_area

    # 큰 사각형에서 작은 사각형을 뺌
    area = melon_area[l1] * melon_area[l2] - (melon_area[s1] * melon_area[s2])

    # 참외 수를 곱함
    melon = area * n

    return melon


N = int(input())

my_melon = []
for i in range(6):
    my_melon += list(map(int, input().split()))

# 방향을 담은 리스트, 면적을 담은 리스트를 넘겨주기 위해서
# 만든 리스트를 두 개로 쪼개서 방향과 면적을 따로 저장
my_melon_dir = []
my_melon_area = []
for i in range(12):
    if i % 2 == 0:
        my_melon_dir.append(my_melon[i])
    else:
        my_melon_area.append(my_melon[i])

print(melon_farm(N, my_melon_dir, my_melon_area))
