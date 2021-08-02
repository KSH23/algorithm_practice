# 2628. 종이자르기


def find_max_area(col, row, cut_list):
    # 잘라지는 가로, 세로 선을 담는 리스트
    row_list = [0, row]
    col_list = [0, col]

    # 잘라지는 가로, 세로 선을 리스트에 담음
    for cut in cut_list:
        if cut[0] == 0:
            row_list.append(cut[1])
        else:
            col_list.append(cut[1])

    # 잘릴 가로, 세로 선을 오름차순으로 정렬
    row_list.sort()
    col_list.sort()

    area = 0
    max_area = 0

    # 이중 for문을 돌며 각 잘린 종이의 크기를 재고 최댓값을 구함
    for i in range(len(row_list)-1):
        for j in range(len(col_list)-1):
            area = (row_list[i+1] - row_list[i]) * (col_list[j+1] - col_list[j])
            if area > max_area:
                max_area = area

    return max_area


# 종이의 가로, 세로 길이
n, m = map(int, input().split())

# 자를 번호들을 리스트로 만든 후 리스트에 담음
cut_no = int(input())
my_cut_list = []
for i in range(cut_no):
    my_cut_list.append(list(map(int, input().split())))

print(find_max_area(n, m, my_cut_list))
