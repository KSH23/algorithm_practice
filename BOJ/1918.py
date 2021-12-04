# 1918. 후위 표기식


notation = input()
stack = []

# 각 연산자의 우선순위를 설정
operations = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 0}
ans = ''  # 최종 결과
for char in notation:
    if char in operations:  # 연산자의 경우
        # 스택이 비어있거나 여는 괄호면 바로 추가
        if not stack or char == '(':
            stack.append(char)
            continue

        # 닫는 괄호는 여는 괄호가 나올 때 까지 연산자를 최종 결과로 이동
        if char == ')':
            while stack[-1] != '(':
                ans += stack.pop()
            stack.pop()  # 여는 괄호 제거
            continue

        # 현재 char보다 우선순위가 크거나 같은 연산자는 최종 결과로 이동
        while stack and operations[char] <= operations[stack[-1]]:
            ans += stack.pop()
        stack.append(char)  # 연산자를 스택에 추가

    else:  # 피연산자의 경우 최종 결과에 바로 추가
        ans += char

while stack:  # 스택에 남은 연산자를 최종 결과에 추가
    ans += stack.pop()

print(ans)