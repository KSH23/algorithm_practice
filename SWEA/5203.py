# 5203. 베이비진 게임


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    team = [[], []]  # 각 팀별 카드 목록
    cnt_list = [[0] * 10, [0] * 10]  # 각 팀별 카드 개수 리스트
    switch = 0  # 승자가 나올 시 승자 번호 표시
    for turn in range(6):
        if switch > 0:  # 승자가 나오면 게임 종료
            break
        for team_num in range(2):  # 두 팀이 순서대로 진행
            if switch > 0:  # 만약 승자가 나오면 게임 종료
                break

            card = cards[turn * 2 + team_num]  # 카드 선택
            team[team_num].append(card)  # 카드 리스트에 카드 추가
            cnt_list[team_num][card] += 1  # 카드 개수 리스트 갱신

            idx = 0  # 베이비진 검사를 시작할 인덱스
            while len(team[team_num]) >= 3 and idx < 10:
                if cnt_list[team_num][idx] >= 3:  # triplet 검사
                    switch = team_num + 1
                    break

                if idx <= 7:  # run 검사
                    for i in range(idx, idx + 3):
                        if cnt_list[team_num][i] == 0:
                            break
                    else:
                        switch = team_num + 1
                        break
                idx += 1

    print(f'#{tc} {switch}')