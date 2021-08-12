# 13300. 방 배정


def room(k, students):
    # 한 학년당 [0, 0] 리스트를 만들고 인덱스 계산을 하지 않기 위해 0학년도 추가
    total_room = [[0, 0] for _ in range(7)]

    # 각 학생을 방에 넣음
    for student in students:
        total_room[student[1]][student[0]] += 1

    room_num = 0    # 필요한 방의 수
    for i in range(7):
        for j in range(2):
            if total_room[i][j]:    # 방에 0이 아닌 수가 있다면

                # 필요한 방의 수를 최대 학생 인원에 따라 계산하여 추가
                room_num += (total_room[i][j] + k - 1) // k

    return room_num


N, K = map(int, input().split())
my_students = [list(map(int, input().split())) for _ in range(N)]
print(room(K, my_students))