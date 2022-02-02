# 62048. 멀쩡한 사각형


def solution(w, h):
    answer = w * h
    w, h = min(w, h), max(w, h)  # 계산의 편의를 위해 w <= h로 설정

    cnt = 0  # 사용할 수 없는 종이의 개수
    col = 1  # x 좌표가 col을 넘을 때마다 cnt가 한 개 더 추가

    # 종이를 위쪽 반만 검사하고 이후 2배를 하도록 함
    for row in range(1, h // 2 + 1):
        x = (w / h) * row  # 현재 x 좌표

        # x 좌표가 이동할 때마다 하나의 종이를 사용 못하며
        # col을 넘으면 하나의 종이를 추가로 더 사용 못함
        if x < col:
            cnt += 1
        elif col < x:
            col += 1
            cnt += 2

        # x 좌표가 col과 일치하는 경우 w와 h는 1이 아닌 최대 공약수를 갖고
        # 현재까지 사용할 수 없는 종이의 개수의 배수를 사용 못함
        # 이후 사용할 수 없는 종이의 개수를 2배 할 필요도 없음
        else:
            cnt += 1
            cnt *= h // row
            break

    else:
        cnt *= 2

        # 만약 h와 w가 홀수인 경우 정 가운데에서 하나의 종이를 지나며
        # h가 홀수이고 w가 짝수인 경우 정 가운데에서 두 개의 종이를 지남
        if h % 2:
            if w % 2:
                cnt += 1
            else:
                cnt += 2

    return answer - cnt


print(solution(3, 5))