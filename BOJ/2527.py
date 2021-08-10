# 2527. 직사각형


def check_square(square_list):
    # x좌표가 작은 사각형을 s1, 나머지 사각형을 s2로 설정
    if square_list[0] <= square_list[4]:
        s1 = square_list[:4]
        s2 = square_list[4:]
    else:
        s1 = square_list[4:]
        s2 = square_list[:4]

    # 만약 작은 사각형의 우측벽 너머에 큰 사각형의 좌측 벽이 있다면 곂치지 않음
    if s1[2] < s2[0]:   
        return 'd'

    # 큰 사각형이 작은 사각형보다 높거나 낮게 있으면 곂치지 않음
    elif s1[3] < s2[1] or s1[1] > s2[3]:
        return 'd'

    # 만약 작은 사각형의 우측벽이 큰 사각형의 좌측벽일 경우
    elif s1[2] == s2[0]:
        # 큰 사각형의 꼭지점이 작은 사각형의 꼭지점인 경우
        if s1[3] == s2[1] or s1[1] == s2[3]:
            return 'c'
        
        else:    # 위 경우가 아니라면 무조건 곂침
            return 'b'

    # 큰 사각형의 좌측벽 이후에 작은 사각형 우측벽이 등장하는 경우
    else:
        # 각 사각형의 위, 아래 벽이 서로 만나는 경우
        if s1[3] == s2[1] or s1[1] == s2[3]:
            return 'b'
        
        else:    # 위 경우가 아니라면 무조건 곂침
            return 'a'
   

my_square_list = []
for i in range(4):
    my_square_list = list(map(int, input().split()))
  
    print(check_square(my_square_list))