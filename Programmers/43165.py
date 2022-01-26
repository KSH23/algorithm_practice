# 43165. 타켓 넘버


from collections import deque


def solution(numbers, target):
    answer = 0
    q = deque([0])  # 초기값 0 설정
    idx = 0  # 더하거나 뺄 숫자의 인덱스
    while q:
        # for loop를 이용하여 같은 idx에서 추가된 수만 함께 고려
        for _ in range(len(q)): 
            cur_num = q.popleft()
            
            # 모든 수를 고려하였고 그 중 target을 만난 경우 
            if idx == len(numbers) and cur_num == target:
                answer += 1
                
            if idx < len(numbers):
                q.append(cur_num + numbers[idx])  # 숫자 더하기
                q.append(cur_num - numbers[idx])  # 숫자 빼기
        idx += 1

    return answer


print(solution([1, 1, 1, 1, 1], 3))