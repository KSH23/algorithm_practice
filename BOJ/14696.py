# 14696. 딱지놀이


def winner(a, b):
    a_shape = a[1:]    # a의 카드 모양만 남김
    b_shape = b[1:]    # b의 카드 모양만 남김

    a_check = [0, 0, 0, 0, 0]    # 각 카드 모양의 수를 셀 리스트 생성
    b_check = [0, 0, 0, 0, 0]    # 맨 앞 0은 인덱스 = 카드번호 맞추기 위해 추가

    for shape in a_shape:
        a_check[shape] += 1    # a의 각 카드 수 저장
    for shape in b_shape:
        b_check[shape] += 1    # b의 각 카드 수 저장

    # a의 카드 수 리스트에서 b의 카드 수 리스트를 뺌
    for i in range(5):
        a_check[i] = a_check[i] - b_check[i]

    # 4, 3, 2, 1 순으로 반복하면서 승자 검사
    for i in range(4, 0, -1):
        if a_check[i] == 0:    # 카드 수가 같은 경우 다시 반복문 시작
            continue
        else:
            if a_check[i] > 0:    # 만약 양수라면 a가 더 많이 가지고 있으므로
                return 'A'    # a가 이김
            else:    # 만약 음수라면 b가 더 많이 가지고 있으므로
                return 'B'    # b가 이김

    return 'D'    # 여기까지 왔다면 누구도 이기지 않았으므로 비김


N = int(input())

for i in range(N):
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    print(winner(a_list, b_list))