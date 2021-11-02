# 16953. A → B


from collections import deque


def bfs():
    q = deque()
    q.append((A, 1))  # 초기값 설정 (숫자, 연산 횟수)

    while q:
        number, cnt = q.popleft()
        
        # 2를 곱한 값, 1을 오른쪽에 추가한 값
        for new_num in [number * 2, number * 10 + 1]:
            if new_num == B:  # 원하는 값을 찾은 경우
                return cnt + 1
            if B < new_num:
                continue  # 원하는 값을 초과하면 그 이후는 고려하지 않음
            q.append((new_num, cnt + 1))
            
    # 만들 수 없는 경우
    return -1


A, B = map(int, input().split())
print(bfs())