# 10773.제로


K = int(input())
stack = []
for _ in range(K):
    number = int(input())
    if number:
        stack.append(number)
    else:
        stack.pop()

print(sum(stack))