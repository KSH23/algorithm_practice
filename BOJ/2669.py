# 2669. 직사각형 네개의 합집합의 면적 구하기


# 두 개의 좌표를 갖는 리스트를 담은 리스트를 받아 면적을 구하는 함수
def find_area(coord_list):
    # 100x100의 크기를 갖는 격자 생성
    grid = []
    for i in range(100):
        one_line = []
        for j in range(100):
            one_line.append(0)
        grid.append(one_line)

    area_count = 0    # 면적을 세는 변수

    # 여러 좌표들을 차례로 확인
    for coord in coord_list:
        # 두 개의 좌표로 만들어진 사각형을 확인
        for x in range(coord[0], coord[2]):    
            for y in range(coord[1], coord[3]):
                # 만약 사각형 안에 0이 있다면 1로 바꾸고 카운트함
                # 이후 중복된 좌표가 나와도 이미 1로 바뀐 상태라 카운트 하지 않음
                if grid[y][x] == 0:
                    grid[y][x] = 1
                    area_count += 1

    return area_count


# 주어지는 좌표들을 하나의 리스트로 정리
my_coord_list = []
for i in range(4):
    my_coord_list.append(list(map(int, input().split())))

print(find_area(my_coord_list))