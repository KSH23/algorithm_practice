"""
5431: 민석이의 과제 체크하기
"""

import sys
sys.stdin = open('5431_input.txt')


def ab_students(n, students):
    # 총 학생 리스트 생성
    students_list = list(range(1, n+1))
    
    # 리스트에서 과제 제출 학생 제거
    for student in students:
        students_list.remove(student)
    
    # return에서 .join()을 쓰기 위해 학생 번호를 int에서 str로 변환
    students_str = list(map(str, students_list))
    
    return ' '.join(students_str)


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    my_student = list(map(int, input().split()))

    print(f'#{tc} {ab_students(N, my_student)}')