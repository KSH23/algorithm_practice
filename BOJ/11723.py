# 11723. 집합


import sys


S = 0  # 각 결과를 비트마스킹으로 저장
M = int(sys.stdin.readline())
for _ in range(M):
    command = sys.stdin.readline().split()
    if len(command) > 1:
        num = int(command[1])
        if command[0] == 'add':
            S |= 1 << num
        elif command[0] == 'remove':
            # 해당 숫자만 0으로 만든 뒤 and 연산으로 제거
            S &= ((1 << 21) - 1) ^ 1 << num
        elif command[0] == 'check':
            # 해당 숫자 자리 좌측은 (1 << num)으로 제거하고
            # 우측은 >> num 연산으로 제거한 뒤 출력
            print((S & 1 << num) >> num)
        elif command[0] == 'toggle':
            S ^= 1 << num
    elif command[0] == 'all':
        S = (1 << 21) - 1
    elif command[0] == 'empty':
        S = 0