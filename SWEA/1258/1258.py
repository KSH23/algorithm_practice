"""
1258: 행렬찾기
"""

import sys
sys.stdin = open('1258_input.txt')


# 두 개의 좌표가 담긴 리스트와 행렬을 넘기면 두 좌표 사이의 모든 값을 0으로 바꾸는 함수
def clear_matrix(location_list, matrix):
    for i in range(location_list[0], location_list[2]):
        for j in range(location_list[1], location_list[3]):
            matrix[i][j] = 0
    return matrix


# 2개의 원소를 갖는 리스트를 원소로 갖는 리스트를 넘기면
# 2개의 원소를 곱한 값을 기준으로 오름차순 정렬하는 함수
def max_multiple(num_list):
    for i in range(len(num_list)):
        for j in range(len(num_list)-1):
            if num_list[j][0] * num_list[j][1] > num_list[j+1][0] * num_list[j+1][1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

            # 만약 곱한 값이 서로 같으면 행이 작은 수가 앞에 오도록 함
            elif num_list[j][0] * num_list[j][1] == num_list[j+1][0] * num_list[j+1][1]:
                if num_list[j][0] > num_list[j+1][0]:
                    num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list


# 행렬과 그 길이를 넘기면 원소가 0이 아닐때 위 두 함수를 실행시키는 메인 함수
def find_matrix(N, matrix):
    # 숫자 부분행렬의 길이들을 저장할 리스트
    result_list = []

    # 행렬을 수직방향, 수평방향으로 검사
    for v in range(N):
        for h in range(N):
            # 숫자를 발견하면 나중에 clear_matrix에 넘겨
            # 0으로 만들기 위해 필요한 좌표를 저장하는 변수
            clear_mat = []

            # 숫자를 발견하면 처리 시작
            if matrix[h][v] != 0:
                # 처음 숫자가 나온 좌표를 넘김
                clear_mat.extend([h, v])

                # 숫자 부분행렬의 길이를 저장하기 위한 리스트
                len_list = []

                # 다시 0을 만나는 지점이 숫자 부분행렬의 길이
                for j in range(h, N):
                    if matrix[j][v] == 0 or j == N-1:
                        len_list.append(j-h)   
                        
                        # 다시 0을 만나면 그 때의 좌표 또한 저장
                        clear_mat.append(j)  
                        break 

                # 숫자 부분행렬의 열도 위와 마찬가지
                for i in range(v, N):           
                    if matrix[h][i] == 0 or i == N-1:
                        len_list.append(i-v)
                        clear_mat.append(i)
                        break
                
                # 부분행렬의 길이를 저장 후 
                result_list.append(len_list)
                # 이미 계산한 숫자 부분행렬은 0으로 만든 뒤 처음부터 반복
                matrix = clear_matrix(clear_mat, matrix)
    
    # 결과를 문제에서 요구하는 방식으로 정렬
    result_list = max_multiple(result_list)
    
    return result_list


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    
    # 행렬 만들기
    my_matrix = []
    for i in range(n):
        my_matrix.append(list(map(int, input().split())))

    result = find_matrix(n, my_matrix)

    # 최종 결과 리스트를 문제에서 요구하는 방식으로 출력하기 위해
    # 이중 리스트를 풀어 숫자만을 요소로 갖는 리스트로 만듦
    pretty_result = []
    for i in range(len(result)):
        for j in range(2):
            pretty_result.append(result[i][j])
    
    print(f'#{tc} {len(result)} {" ".join(map(str, pretty_result))}')