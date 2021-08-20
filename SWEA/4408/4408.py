# 4408. 자기 방으로 돌아가기


def go(room_list):
    # result 리스트를 생성 후 한꺼번에 움직일 수 있는 방을 리스트에 모두 담고
    # 이를 result에 넣으면 최종 결과는 result의 길이가 됨

    for room in room_list:    # 무조건 room[0]이 작은 수가 되게 만듦
        if room[0] > room[1]:
            room[0], room[1] = room[1], room[0]

    room_list.sort()    # 방을 room[0]을 기준으로 정렬
    result = [[room_list[0]]]    # 최종 방 구조를 담는 리스트

    for room in room_list[1:]:
        flag = 0
        for i in range(len(result)):
            # 리스트 다음에 들어올 수 있는 방은 room[0]이 앞 칸의 room[1]보다 작아야 하고
            # room[0]이 홀수일 때에는 이전 방보다 한 칸만 높은 수여도 되지만
            # room[0]이 짝수일 때에는 이전 방보다 두 칸 높은 수여야 하기 때문에
            # (1 - room[0] % 2)을 더해줌
            if room[0] > result[i][-1][-1] + (1 - room[0] % 2):
                result[i] += [room]
                break
            else:    # 만약 리스트 다음에 들어올 수 없다면 flag를 1 증가
                flag += 1
        if flag == len(result):    # 여기까지 왔다면 result[i]에 속하지 못한 것이므로
            result += [[room]]    # result[i+1]을 직접 만들어줌

    # 최종 결과는 result에 만들어진 리스트의 개수가 됨
    return len(result)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    my_room_list = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(tc, go(my_room_list)))