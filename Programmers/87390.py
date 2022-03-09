# 87390. n^2 배열 자르기


def solution(n, left, right):
    answer = []
    
    # 배열에 적히는 숫자는 인덱스에 따라 행과 열의 크기에 따른 규칙을 가짐
    for index in range(int(left), int(right) + 1):
        row = index // n
        col = index % n
        
        if row <= col:  # 행보다 열이 크거나 같은 경우 열의 숫자를 가짐
            answer.append(col + 1)
        else:  # 행이 열보다 큰 경우 행의 숫자를 가짐
            answer.append(row + 1)

    return answer