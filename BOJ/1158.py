# 1158. 요세푸스 문제


N, K = map(int, input().split())

Q = list(range(N))
start = 0
ans = []

while len(Q) > 0:
    start = (start + K - 1) % len(Q)
    ans += [Q.pop(start) + 1]
    
print(f'<{", ".join(map(str, ans))}>')
