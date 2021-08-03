# 2116. 주사위 쌓기


def stacking_dice(dice_list):
    max_result = []    # 6번의 실행 결과를 담을 리스트, 이후 여기서 최댓값을 반환할 예정

    bottom = 0    # 주사위 아랫면
    top = 0    # 주사위 윗면

    # 문제의 그림을 잘 못 이해해서 인덱스의 합이 5가 된다면 서로 마주 보는 면이라는 착각을 함
    # 차라리 착각을 발전 시켜 마주 보는 면끼리의 인덱스 합이 5가 되도록 만들 예정
    # [3] 요소와 [4] 요소를 뒤바꾸면 마주 보는 면의 인덱스 합은 5가 됨
    # 아래 코드를 첫번째 for문 안에 넣어서 계속 틀렸는데, 반복하며 서로 계속 뒤바뀌었던 것이 문제였을 듯
    dice_list[0][3], dice_list[0][4] = dice_list[0][4], dice_list[0][3]

    # 1번 주사위의 아랫면이 될 수 있는 6번의 경우의 수
    for idx in range(6):
        # 각 리스트는 복사해서 사용할 예정
        # 이후 리스트에서 위, 아래 인덱스를 삭제할 것인데 복사를 하지 않으면 기존 리스트도 영향을 받음
        dice_one = dice_list[0][:] 

        max_this_time = 0    # 이번 경우(idx)의 최댓값

        bottom = dice_list[0][idx]    # 1번 주사위의 아랫면
        top = dice_list[0][5 - idx]    # 1번 주사위의 윗면

        # 1번 주사위의 옆면만 남긴 후 남은 주사위 번호 중 최댓값 저장
        dice_one.remove(bottom)
        dice_one.remove(top)
        max_this_time += max(dice_one)      

        for dice in dice_list[1: ]:    # 2번 주사위부터 반복 시작
            c_dice = dice[:]    # 주사위 복사
            c_dice[3], c_dice[4] = c_dice[4], c_dice[3]
           
            for i in range(6):    
                if c_dice[i] == top:    # 만약 아래 주사위의 윗면과 같다면
                    bottom = top    # 기존의 윗면은 아랫면이 되고
                    top = c_dice[5-i]    # 기존의 윗면은 새로운 윗면이 됨
      
                    # 주사위의 윗면과 아랫면을 제외한 숫자를 리스트에 넣음
                    c_dice.remove(top)
                    c_dice.remove(bottom)
                    max_this_time += max(c_dice)
                    break
        
        max_result.append(max_this_time)    # 이번 경우의 최댓값을 저장

    # 최종 결과들을 담은 리스트에서 최댓값을 반환
    return max(max_result)


my_dice_no = int(input())

# 주사위 리스트를 리스트 안에 넣음
my_dice_list = []
for i in range(my_dice_no):
    my_dice_list.append(list(map(int, input().split())))

print(stacking_dice(my_dice_list))