# 42587. 프린터


from collections import deque


def solution(priorities, location):
    q = deque(list(range(len(priorities))))  # 인덱스로 구성된 덱
    stack = []
    
    while q:
        num = q.popleft()  # 현재 숫자
        
        temp = []  # 다시 뒤로 돌아가야 할 숫자 리스트
        while stack and priorities[stack[-1]] < priorities[num]:
            # 중요도가 낮은 인덱스는 스택에 쌓인 순서대로 temp에 저장
            last_num = stack.pop()
            temp.append(last_num)
        
        # temp에 저장된 인덱스를 역으로 빼내며 덱에 다시 추가
        while temp:
            q.append(temp.pop())

        stack.append(num)  # 현재 숫자를 덱에 추가

    # (찾는 인덱스 값이 stack 리스트에서 갖는 인덱스) + 1을 반환
    return stack.index(location) + 1