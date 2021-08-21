# 2615. 오목


def find_winner(omok):
    di = [0, 1, 1, -1]    # row의 우, 우하향, 하, 우상향
    dj = [1, 1, 0, 1]    # col의 우, 우하향, 하, 우상향

    for i in range(19):
        for j in range(19):
            # 1. 오목의 칸들을 돌면서 0이 아닌 수가 적힌 칸을 발견하면 검사 시작
            if omok[i][j] == 0:
                continue

            flag = 1    # 이 값이 5가 되면 일단 5개는 완성되었다는 의미

            for k in range(4):
                # 2. 지금 칸에서 우향, 우하향, 하향, 우상향을 차례로 검사하면서
                #    만약 검사한 다음 칸이 오목 판 밖을 나가거나
                #    다음 칸의 숫자가 현재 내가 찾고 있는 숫자와 같지 않다면 무시
                if i + di[k] < 0 or 18 < i + di[k] or j + dj[k] < 0 or 18 < j + dj[k]:
                    continue
                if omok[i + di[k]][j + dj[k]] != omok[i][j]:
                    continue

                for l in range(1, 5):
                    # 3. 연속으로 놓인 돌을 찾으면 그 이후로 4번을 더 검사하여 총 5개가 되는지 확인
                    #    만약 4번을 검사하기 전에 오목 판 밖을 나가거나
                    #    내가 찾는 숫자와 같지 않다면 이 for문을 탈출
                    #    위 두 조건에 해당하지 않는다면 flag를 하나씩 올림
                    if 18 < i + di[k] * l or j + dj[k] * l < 0 or 18 < j + dj[k] * l:
                        flag = 1
                        break
                    if omok[i + di[k] * l][j + dj[k] * l] != omok[i][j]:
                        flag = 1
                        break
                    flag += 1

                # 4. 만약 위 for문을 전부 돌았다면 flag는 5가 되고
                #    이전, 이후의 돌을 검사하여 5개가 넘는 돌이 연속으로 놓였는지를 검사
                #    따라서 만약 이후의 돌이 오목 판을 나가지 않았는데 현재 찾는 돌과 숫자가 같은 경우,
                #    또는 이전의 돌이 오목 판을 나가지 않았는데 현재 찾는 돌과 숫자가 같은 경우
                #    flag를 1로 만듦
                if flag == 5:
                    if 0 <= i + di[k] * 5 < 19 and 0 <= j + dj[k] * 5 < 19:
                        if omok[i + di[k] * 5][j + dj[k] * 5] == omok[i][j]:
                            flag = 1
                    if 0 <= i - di[k] < 19 and 0 <= j - dj[k] < 19:
                        if omok[i - di[k]][j - dj[k]] == omok[i][j]:
                            flag = 1

                # 5. 여기서 여전히 flag가 5라면 모든 조건을 만족시킨 경우이므로 원하는 값 return
                if flag == 5:
                    return [omok[i][j], i+1, j+1]

    # 6. 만약 여기까지 도착했다면 원하는 경우를 모두 찾지 못한 것이므로 0을 return
    return [0]    # 이후 출력을 용이하기 위해 위와 같은 형태인 list로 return


my_omok = [list(map(int, input().split())) for _ in range(19)]
ans = find_winner(my_omok)
print(ans[0])    # 승부의 결과를 인쇄
if len(ans) > 1:    # 만약 반환받은 값이 한 개를 넘는다면 위치를 받은 것이므로 이를 함께 출력
    print(' '.join(map(str, ans[1:])))