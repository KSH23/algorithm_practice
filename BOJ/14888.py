# 14888. 연산자 끼워넣기


def do_operate(stack_list):    # 매개변수로 연산 목록을 받는 연산 실행 함수
    global min_ans, max_ans

    numbers_list = num_list[:]    # 숫자 목록을 복사한 리스트
    operate_list = stack_list[:]    # 연산 목록을 복사한 리스트

    while len(numbers_list) > 1:
        num1 = numbers_list.pop(0)    # 앞의 숫자
        num2 = numbers_list.pop(0)    # 뒤의 숫자
        operation = operate_list.pop(0)    # 실행할 연산자
        if operation == 0:    # 0은 덧셈
            numbers_list = [num1 + num2] + numbers_list
        elif operation == 1:    # 1은 뺄셈
            numbers_list = [num1 - num2] + numbers_list
        elif operation == 2:    # 2는 곱셈
            numbers_list = [num1 * num2] + numbers_list
        elif operation == 3:    # 3은 나눗셈
            if num2 == 0:
                return    # 0으로 나눌수 없으므로 함수 종료
            if num1 < 0 < num2 or num2 < 0 < num1:    # 음수가 포함된 나눗셈의 경우
                numbers_list = [-(abs(num1) // abs(num2))] + numbers_list
            else:
                numbers_list = [num1 // num2] + numbers_list

    if numbers_list[0] < min_ans:    # 연산 결과를 토대로 최솟값 갱신
        min_ans = numbers_list[0]
    if max_ans < numbers_list[0]:    # 연산 결과를 토대로 최댓값 갱신
        max_ans = numbers_list[0]

    return


def make_stack():    # 연산 리스트를 생성하는 함수
    global stack, pre, used_idx
    # stack: 연산자가 쌓이는 리스트
    # pre: 이전 단계에서의 스택을 복사한 리스트
    # sed_idx: 사용된 인덱스를 기록할 리스트

    if len(stack) == N - 1:    # 연산자 리스트를 완성한 경우
        do_operate(stack)    # 연산 실행 함수를 호출
        return

    # 기존에 생성한 연산자 리스트를 돌면서 새로운 연산자 리스트 생성
    for i in range(len(operation_list)):
        if used_idx[i] == 1:    
            continue    # 이미 사용한 연산자는 무시

        stack += [operation_list[i]]    # 스택에 연산자 추가
        
        # 만약 현재 스택과 이전 단계 스택이 같다면 더 이상 진행할 필요 없음
        if stack == pre:
            stack.pop()    # 넣었던 원소는 다시 제거
            continue
        used_idx[i] = 1    # 사용한 인덱스 기록
        make_stack()    
        pre = stack[:]    # 현재 스택을 이전 단계 스택으로 기록
        stack.pop()    # 넣었던 원소 제거
        used_idx[i] = 0    # 사용했던 기록 제거


N = int(input())
num_list = list(map(int, input().split()))    # 숫자 리스트
operation_cnt_list = list(map(int, input().split()))

operation_list = []    # 연산자를 숫자로 저장할 리스트
for idx in range(len(operation_cnt_list)):
    # 0은 덧셈, 1은 뺄셈, 2는 곱셈, 3은 나눗셈으로 저장
    operation_list += [idx] * operation_cnt_list[idx]

stack = []    # 스택 생성
used_idx = [0] * (N - 1)    # 사용한 인덱스를 기록할 리스트 생성
min_ans, max_ans = 10**9, -10**9    # 최솟값, 최댓값 초기화
pre = []    # 이전 단계에서의 스택을 복사할 리스트

make_stack()
print(max_ans)
print(min_ans)