# 1244. 스위치 켜고 끄기


def turn_switch(num):    # 스위치 켜고 끄는 함수
    if num == '1':
        return '0'
    else:
        return '1'


def student_switch(switch_list, students_list):
    switch_list = ['2'] + switch_list    # 스위치 번호와 인덱스 번호 일치

    for student in students_list:
        if student[0] == 1:    # 남학생이 하는 일
            for i in range(1, len(switch_list)):
                if i % student[1] == 0:
                    switch_list[i] = turn_switch(switch_list[i])

        else:    # 여학생이 하는 일
            s_idx = student[1]    # 여학생이 받은 수
            switch_list[s_idx] = turn_switch(switch_list[s_idx])    # 여학생이 받은 수는 무조건 바뀜

            limit = min(s_idx, len(switch_list) - s_idx)    # 여학생이 받은 수에서 대칭 한계점

            for i in range(1, limit):    # 좌우 대칭이 같으면 스위치 전환
                if switch_list[s_idx - i] == switch_list[s_idx + i]:
                    switch_list[s_idx - i] = turn_switch(switch_list[s_idx - i])
                    switch_list[s_idx + i] = turn_switch(switch_list[s_idx + i])
                else:
                    break

    return switch_list[1:]    # 맨 처음 넣은 맨 앞의 2 제외하고 반환

# 스위치 개수, 스위치 리스트, 학생 수, 학생 리스트를 변수로 받음
my_switch_num = int(input())
my_switch_list = list(input().split())
my_students_num = int(input())
my_students_list = []

# 학생 수 만큼 학생 리스트 안에 리스트로 넣음
for i in range(my_students_num):
    my_students_list.append(list(map(int, input().split())))

# 최종 결과 리스트
result = student_switch(my_switch_list, my_students_list)

# 최종 결과를 20개씩 나눠 출력
for i in range(len(result) // 20 + 1):
    if len(result) < 20:
        print(' '.join(result))
    else:
        print(' '.join(result[0: 20]))
        result = result[20: ]
      