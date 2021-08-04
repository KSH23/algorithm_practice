# 2578. 빙고


def count_bingo(bingo):
    # 빙고 수를 세는 함수
    # 만약 한 줄의 합이 0이면 bingo_count가 하나 오름    
    bingo_count = 0
  
    for i in range(5):    # 가로줄 빙고
        check_sum = 0
        for j in range(5):
            check_sum += bingo[i*5 + j]
        if check_sum == 0:
            bingo_count += 1

    for i in range(5):    # 세로줄 빙고
        check_sum = 0
        for k in range(5):
            check_sum += bingo[i + k * 5]
        if check_sum == 0:
            bingo_count += 1
    
    check_sum = 0        
    for l in range(5):    # \ 대각선 빙고
        check_sum += bingo[6*l]
    if check_sum == 0:
            bingo_count += 1
    
    check_sum = 0
    for m in range(5):    # / 대각선 빙고
        check_sum += bingo[4*(m+1)]
    if check_sum == 0:
            bingo_count += 1
    
    return bingo_count


def find_bingo(bingo, ans_bingo):    # 정답 체크하는 함수
    for i in range(25):
        for j in range(25):
            if bingo[j] == ans_bingo[i]:
                bingo[j] = 0    # 체크된 칸은 0으로 만듦

                # 빙고가 3개 이상 나오는 순간 함수 끝
                if count_bingo(bingo) >= 3: 
                    return i + 1
        

my_bingo = []    # 내 빙고를 한 줄로 저장
for i in range(5):
    my_bingo += list(map(int, input().split()))

my_ans_bingo = []    # 정답 숫자들을 한 줄로 저장
for i in range(5):
    my_ans_bingo += list(map(int, input().split()))

print(find_bingo(my_bingo, my_ans_bingo))