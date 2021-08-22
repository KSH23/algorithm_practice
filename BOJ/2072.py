# 2072. 오목


def find_winner(omok):    # 2615번의 함수 응용
    di = [0, 1, 1, -1]    # row의 우, 우하향, 하, 우상향
    dj = [1, 1, 0, 1]    # col의 우, 우하향, 하, 우상향

    for i in range(19):
        for j in range(19):
            if omok[i][j] == 0:
                continue

            flag = 1    # 이 값이 5가 되면 일단 5개는 완성되었다는 의미

            for k in range(4):
                if i + di[k] < 0 or 18 < i + di[k] or j + dj[k] < 0 or 18 < j + dj[k]:
                    continue
                if omok[i + di[k]][j + dj[k]] != omok[i][j]:
                    continue

                for l in range(1, 5):
                    if 18 < i + di[k] * l or j + dj[k] * l < 0 or 18 < j + dj[k] * l:
                        flag = 1
                        break
                    if omok[i + di[k] * l][j + dj[k] * l] != omok[i][j]:
                        flag = 1
                        break
                    flag += 1

                if flag == 5:
                    if 0 <= i + di[k] * 5 < 19 and 0 <= j + dj[k] * 5 < 19:
                        if omok[i + di[k] * 5][j + dj[k] * 5] == omok[i][j]:
                            flag = 1
                    if 0 <= i - di[k] < 19 and 0 <= j - dj[k] < 19:
                        if omok[i - di[k]][j - dj[k]] == omok[i][j]:
                            flag = 1

                if flag == 5:
                    return True

    return False


N = int(input())
my_omok = [[0] * 19 for _ in range(19)]
winner = 0    # 이기는 순간의 수를 저장할 변수

for turn in range(N):
    i, j = map(int, input().split())
    
    # 오목 판에 (turn + 1)이 홀수일 때에는 1을 놓고
    # 짝수일 때에는 2를 놓은 후 매 번 승자를 찾는 함수 실행
    my_omok[i-1][j-1] = 2 - (turn + 1) % 2
    
    # 만약 함수를 통해 승자를 찾았다면 이 때의 수를 저장 후 break
    if find_winner(my_omok):
        winner = turn + 1
        break

if winner > 0:    # 승자를 찾았다면 수를 출력
    print(winner)
else:    # 승패가 갈리지 않는 경우 -1을 출력
    print(-1)