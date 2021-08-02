# 2635. 수 이어가기


def making_numlist(number):
    max_list = []    # 최종 결과 리스트를 저장하는 변수
    
    # 주어진 범위 내위 수를 모두 돌며 하나하나 확인할 예정
    for random_num in range(1, 30001):
        max_length = len(max_list)    # 숫자들의 개수를 세는 변수
        result_list = [number, random_num]    # 숫자를 담는 리스트
        idx = 0    # 리스트의 인덱스 담당 변수
        while True:
            new_number = result_list[idx] - result_list[idx + 1]

            # 새로 만든 숫자가 음수라면 break
            if new_number < 0:
                break

            # break되지 않았다면 새 숫자를 리스트에 넣음
            result_list.append(new_number)
            # 인덱스 하나 추가 후 while 다시 반복
            idx += 1

        # 만들어진 리스트의 길이를 측정해 최댓값을 찾음    
        if max_length < len(result_list):
            max_list = result_list

    return max_list


n = int(input())

print(len(making_numlist(n)))
print(' '.join(map(str, making_numlist(n))))
