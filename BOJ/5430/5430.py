# 5430. AC


from collections import deque


T = int(input())
for _ in range(1, T+1):
    p = deque(input().rstrip())
    n = int(input())
    ugly_num_list = input().rstrip()
    pretty_num_list = deque()

    flag = 1    # 0일때 콤마, 1일때 숫자가 들어와햐 함
    for item in ugly_num_list:
        if item == '[' or item == ']':
            continue
        if item != ',' and flag == 1:
            pretty_num_list.append(item)

        elif item != ',' and flag == 0:
            temp = pretty_num_list.pop() + item
            pretty_num_list.append(temp)
            continue

        flag = (flag + 1) % 2

    switch = 0    # 배열을 뒤집을때 바뀌는 스위치

    while len(p) > 0:
        operation = p.popleft()
        if operation == 'R':
            switch = (switch + 1) % 2
        elif operation == 'D':
            if len(pretty_num_list) == 0:
                pretty_num_list = 'error'
                break
            if switch == 0:
                pretty_num_list.popleft()
            elif switch == 1:
                pretty_num_list.pop()

    if pretty_num_list == 'error':
        print(pretty_num_list)
    elif switch == 0:
        print(f"[{','.join(pretty_num_list)}]")
    else:
        pretty_num_list.reverse()
        print(f"[{','.join(pretty_num_list)}]")