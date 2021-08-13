# 2309. 일곱 난쟁이


def find_dwarfs(d_li):
    # 난쟁이 키의 총 합을 구한 귀 임의의 두 난쟁이를 선택하여 제외하고
    # 그 값이 100이 되면 해당 난쟁이를 제거할 예정

    total_height = 0    # 아홉 난쟁이 키의 총 합
    for d in d_li:
        total_height += d

    remove_li = []    # 제거할 난쟁이를 담는 리스트
    find = 0    # 제거할 난쟁이를 찾으면 1로 바꾼 후 이중 for문을 나옴

    for i in range(9):
        if find == 1:    # find가 1이라면 제거할 난쟁이를 찾은 것
            break
        for j in range(9):
            if i != j and total_height - d_li[i] - d_li[j] == 100:
                remove_li += [d_li[i], d_li[j]]    # 제거할 난쟁이 저장
                find = 1    # 바깥 for문을 나가기 위한 신호
                break

    # 난쟁이 리스트에서 remove_li에 담긴 난쟁이를 제거
    # .remove()를 사용하지 않기 위해 아래와 같이 시도해봄
    i = 0
    while len(d_li) > 7:    # 난쟁이 수가 7이 될 때까지 반복
        if d_li[i] == remove_li[0] or d_li[i] == remove_li[1]:    # 제거 목표 발견
            if i == 0:    # 만약 맨 처음 요소라면 1번 인덱스부터 다시 저장
                d_li = d_li[1:]
            elif i == len(d_li) -1:    # 만약 맨 끝 요소라면 그 앞 인덱스까지 다시 저장
                d_li = d_li[:-1]
            else:    # 맨 앞, 맨 끝도 아니라면 좌우를 따로 더해서 다시 저장
                d_li = d_li[:i] + d_li[i+1:]
        else:
            i += 1

    for i in range(6):    # 난쟁이를 오름차순 정렬하기 위한 버블정렬
        for j in range(6-i):
            if d_li[j] > d_li[j+1]:
                d_li[j], d_li[j+1] = d_li[j+1], d_li[j]

    return d_li


dwarfs_list = []
for i in range(9):
    dwarfs_list += [int(input())]

for i in range(7):
    print(find_dwarfs(dwarfs_list)[i])