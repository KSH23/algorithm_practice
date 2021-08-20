# 4408. 자기 방으로 돌아가기


def go(room_list):
    corridor = [0] * 201    # 홀수 방과 짝수 방 사이의 복도를 고려
    
    for room in room_list:
        if room[0] > room[1]:    # 이동 경로는 오름차순으로
            room[0], room[1] = room[1], room[0]
            
        # 지나가야 하는 경로를 복도 리스트에 1을 추가하여 표시
        for i in range((room[0] + 1) // 2, (room[1] + 1) // 2 + 1):
            corridor[i] += 1

    ans = 0
    for i in range(len(corridor)):    # 곂치는 최대 수가 최종 결과
        if corridor[i] > ans:
            ans = corridor[i]

    return ans


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    my_room_list = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(tc, go(my_room_list)))