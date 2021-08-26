# 1225. 암호생성기


T = 10
for tc in range(1, T+1):
    N = int(input())
    q = list(map(int, input().split()))

    front = 0
    rear = 7
    minus = 0    # 감소시킬 값, [1, 2, 3, 4, 5]를 반복할 예정

    while True:
        if q[rear] == 0:
            break
        q[front] -= minus + 1
        if q[front] < 0:
            q[front] = 0
        rear = front
        front = (front + 1) % 8
        minus = (minus + 1) % 5

    # front == 0인 상황을 제외하면 rear는 무조건 front의 뒤에 오게 됨
    # 따라서 해당 경우 q를 다시 정렬해줌
    if front != 0:    
        q = q[front:] + q[: rear + 1]
    print('#{} {}'.format(tc, ' '.join(map(str, q))))