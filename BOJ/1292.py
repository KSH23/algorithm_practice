# 1292. 쉽게 푸는 문제


A, B = map(int, input().split())
num_list = [0] * 1001
cur_num = 1
cur_idx = 1
switch = 1

while switch:
    for i in range(cur_num):
        if cur_idx + i == 1001:
            switch = 0
            break
        num_list[cur_idx + i] = cur_num

    cur_idx += cur_num
    cur_num += 1

print(sum(num_list[A: B + 1]))