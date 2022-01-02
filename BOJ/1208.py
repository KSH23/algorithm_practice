# 1208. 부분수열의 합 2


import sys


def subsequence_sum(cur_idx, total_sum, num_list, cnt_dict):
    if cur_idx == len(num_list):
        return

    # 그냥 total_sum 말고 현재 숫자를 더한 경우를 확인해야
    # 중복된 경우의 수를 확인하지 않음
    current_sum = total_sum + num_list[cur_idx]
    cnt_dict[current_sum] = cnt_dict.get(current_sum, 0) + 1

    # 현재 인덱스의 숫자를 포함하는 경우
    subsequence_sum(cur_idx + 1, total_sum + num_list[cur_idx], num_list, cnt_dict)

    # 현재 인덱스의 숫자를 포함하지 않는 경우
    subsequence_sum(cur_idx + 1, total_sum, num_list, cnt_dict)


N, S = map(int, sys.stdin.readline().split())
whole_num_list = list(map(int, sys.stdin.readline().split()))

# 숫자 리스트를 반으로 쪼갠 뒤 각 리스트의 부분 수열의 합을 딕셔너리에 기록
num_list1 = whole_num_list[:N // 2]
sum_cnt1 = {}
num_list2 = whole_num_list[N // 2:]
sum_cnt2 = {}
subsequence_sum(0, 0, num_list1, sum_cnt1)
subsequence_sum(0, 0, num_list2, sum_cnt2)

# 최종 답은 쪼개진 각 리스트에서 S를 만들 수 있는 경우의 수와
# 쪼개진 두 리스트에서 숫자를 합해 S를 만들 수 있는 경우의 수를 합한 것
ans = sum_cnt1.get(S, 0) + sum_cnt2.get(S, 0)
for num_sum, cnt in sum_cnt1.items():
    ans += cnt * sum_cnt2.get(S - num_sum, 0)

print(ans)