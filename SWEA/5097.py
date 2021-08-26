# 5097. 회전


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    front = 0
    rear = N-1

    for i in range(M):
        rear = front
        front = (front + 1) % N

    print('#{} {}'.format(tc, num_list[front]))