# 9375. 패션왕 신해빈


import sys


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    cloth_dict = {}
    for _ in range(N):
        cloth, category = sys.stdin.readline().split()
        # 딕셔너리에 옷 가지수를 넣을 때 이 종류를 입지 않은 경우를
        # 함께 추가하기 위해 초기 값을 1로 설정한다
        cloth_dict.setdefault(category, 1)
        cloth_dict[category] += 1

    ans = 1
    # 이미 딕셔너리의 값에는 해당 종류를 입지 않은 경우도
    # 포함되어 있으므로 모든 값을 곱한다
    for value in cloth_dict.values():
        ans *= value
    
    # 아무것도 입지 않은 경우 한 가지를 제외한다
    print(ans - 1)