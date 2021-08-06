# 2605. 줄 세우기


def make_line(n, students):
    result = []    # 줄을 반대로 세우고 저장할 리스트
    
    for i in range(len(students)):
        for j in range(0, i+1):
            if students[i] == j:
                # 자신이 뽑은 숫자를 기준으로 result의 앞과 뒤를 자르고 그 사이로 들어감
                result = result[0:j] + [i+1] + result[j:]
        
    result.reverse()    # 다시 뒤집으면 최종 결과
    
    return result


N = int(input())

my_students = list(map(int, input().split()))

print(" ".join(map(str, make_line(N, my_students))))