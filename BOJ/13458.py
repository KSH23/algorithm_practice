# 13458. 시험 감독


# 감시 가능한 응시자 수와 학생 수를 받아 최소 감독관 수를 반환하는 함수
def supervisor(b, c, student_num):
    if student_num - b <= 0:    # 만약 총감독관이 모두 감시 가능하면
        case = 0    # 이후 case에는 1이 추가되어 반환될 예정이라 0을 할당
    
    # 총감독관이 감시 가능한 인원을 뺀 나머지 인원이 
    # 부감독관이 감시 가능한 인원과 나누어 떨어진다면 필요한 인원은 몫이 되고
    # 그렇지 않다면 나머지 값 처리를 위해 한 명이 더 필요하다
    elif (student_num - b) % c == 0:
        case = (student_num - b) // c
    else:
        case = (student_num - b) // c + 1

    return case + 1    # 총감독관 한 명을 추가해 반환한다


N = int(input())    # 시험장의 개수
A = list(map(int, input().split()))    # 각 시험장의 응시자 수 리스트
B, C = map(int, input().split())    # 총감독관과 부감독관이 감시 가능한 응시자 수
ans = 0    # 최종 답

for student in A:    # 각 시험장을 돌며 필요 인원을 최종 답에 추가
    ans += supervisor(B, C, student)

print(ans)


'''
1) 학생 수에서 B를 뺐을 때 음수가 나오는 값을 고려 못하여 수정하였다
   아래는 그 반례
   1
   1
   1000000 1
'''