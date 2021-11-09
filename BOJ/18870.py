# 18870. 좌표 압축


import sys


N = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
new_num_list = sorted(num_list)  # 숫자 정렬
num_dict = {}  # 각 숫자의 압축 값을 저장하는 딕셔너리
idx = 0  # 인덱스 == 압축 값
for sorted_num in new_num_list:
    if sorted_num in num_dict:  # 이미 계산했다면 무시
        continue
    num_dict[sorted_num] = idx
    idx += 1

for num in num_list:  # 압축값 출력
    print(num_dict[num], end=' ')
