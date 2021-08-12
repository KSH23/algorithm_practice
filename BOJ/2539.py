# 2539. 모자이크


# 시간이 오래 걸리기 때문에 binary search를 이용한 코드도 짜볼 것
def mosaic(col, n, mistake_list):
    mistake_list.sort()

    # row 기준으로 최소한 색종이의 크기는 가장 높은 row 값보다 커야함
    paper = mistake_list[-1][0]
    col_li = [0] * (col+1)    # col 값만 모을 리스트

    for mistake in mistake_list:
        col_li[mistake[1]] = mistake[1]    # col 리스트

    max_paper = len(col_li) // n + 1    # 최대 색종이 크기

    x = 0    # 현재 위치
    cnt = 0    # 색종이 갯수
    while paper <= max_paper:
        # 만약 현재 위치가 col을 벗어나거나 색종이 갯수가 한계를 넘는다면
        if x >= len(col_li) or cnt > n:
            # 현재 위치가 col을 벗어났는데 색종이를 다 안썼다면 색종이 크기 return
            if cnt <= n:
                return paper
            
            # 색종이가 모자르다면 색종이 크기를 하나 키우고 처음부터 다시 반복
            else:
                paper += 1
                x = 0
                cnt = 0
                continue

        if col_li[x] != 0:    # 실수를 발견했다면 
            # 색종이를 붙여도 col 밖으로 나가지 않는 경우 색종이 크기만큼 x 이동
            if x + paper < len(col_li):
                x += paper
                
            # 색종이를 붙이면 col 밖으로 나가게 된다면 위 if문으로 가 확인하기 위해서
            # x에 일부러 큰 값을 넣음
            else:
                x = len(col_li)
                
            cnt += 1    # 여기까지가 색종이 하나를 위한 반복
        
        else:    # 만약 실수를 발견하지 않았다면 x는 한 칸 이동
            x += 1

    return paper


ROW, COL = map(int, input().split())
N = int(input())    # 사용할 색종이의 장 수
M = int(input())    # 잘못 칠해진 칸의 개수

my_mistake_list = [list(map(int, input().split())) for _ in range(M)]
print(mosaic(COL, N, my_mistake_list))