# 2467. 용액


N = int(input())
solution_list = list(map(int, input().split()))

left, right = 0, N - 1  # 좌측 포인터, 우측 포인터
temp_solution = 10000000000  # 임시 용액 특성
temp_solution_list = [0, 0]  # 사용한 용액 저장 리스트
while left < right:
    solution = solution_list[left] + solution_list[right]  # 현재 용액 정의
    if abs(solution) < abs(temp_solution):  # 임시 용액보다 적은경우
        temp_solution = solution  # 용액 특성 갱신
        temp_solution_list = [solution_list[left], solution_list[right]]

    # 좌측 용액과 우측 용액중 절댓값이 큰 쪽을 없애고 옆으로 이동
    if abs(solution_list[right]) > abs(solution_list[left]):
        right -= 1
    elif abs(solution_list[right]) < abs(solution_list[left]):
        left += 1
    else:  # 좌측 용액과 우특 용액 특성이 같은 경우 0이 되므로 중단
        break

print(f'{temp_solution_list[0]} {temp_solution_list[1]}')