# 10163. 색종이


N = int(input())
paper_list = [list(map(int, input().split())) for _ in range(N)]

grid = [[0] * 1001 for _ in range(1001)]    # 1001x1001 크기 격자 생성

number = 1
for paper in paper_list:    # 격자에 색종이 크기만큼 담당 번호 입력
    for j in range(paper[2]):
        grid[paper[0] + j][paper[1]: paper[1]+paper[3]] = [number] * paper[3]
    number += 1

cnt_list = [0] * N
for i in range(1001):    # 격자를 돌며 담당 번호를 세고 리스트에 담음
    for j in range(1001):
        if grid[i][j] != 0:
            cnt_list[grid[i][j]-1] += 1

for i in range(len(cnt_list)):
    print(cnt_list[i])