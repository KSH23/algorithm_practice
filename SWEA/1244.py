# 1244. 최대 상금


def swap(num_list, idx, swap_cnt):
    # num_list: 현재 숫자 리스트
    # idx: 해당 인덱스의 숫자를 정할 예정

    global ans

    if swap_cnt == int(total_swap_cnt):
        result = ''.join(num_list)
        if ans < result:  # 최댓값 갱신
            ans = result
        return

    if idx == len(num_list):
        # 교환 횟수를 다 채우지 않았는데 리스트의 끝까지 모두 고정한 경우
        remain_swap = int(total_swap_cnt) - swap_cnt
        if remain_swap % 2:  # 교환 횟수가 홀수 번 남은 경우
            # 맨 뒤의 두 원소를 교환한다
            num_list[-1], num_list[-2] = num_list[-2], num_list[-1]
        result = ''.join(num_list)
        if ans < result:  # 최댓값 갱신
            ans = result
        return

    max_str_num = ord('0')  # 최댓값 초기화
    max_i = [0]  # 최댓값의 인덱스가 여러개일 수 있으므로 리스트로 인덱스 저장

    for i in range(idx, len(num_list)):
        if max_str_num < ord(num_list[i]):  # 최댓값 갱신
            max_i = [i]
            max_str_num = ord(num_list[i])
        elif max_str_num == ord(num_list[i]):
            max_i.append(i)  # 최댓값이 여러개인 경우 다른 최댓값도 저장

    if len(max_i) == 1:  # 최댓값을 갖는 숫자가 한 개 있는 경우
        if idx != max_i[0]:  # 그 최댓값의 위치가 지금 위치가 아닐 때에만 교환
            num_list[idx], num_list[max_i[0]] = num_list[max_i[0]], num_list[idx]
            swap(num_list, idx + 1, swap_cnt + 1)  # 다음 위치로 이동
        else:  # 최댓값이 현재 위치에 있다면 교환 없이 넘어감
            swap(num_list, idx + 1, swap_cnt)
    else:  # 최댓값을 갖는 숫자가 여러개인 경우
        for i in max_i:
            if idx != i:  # 현재 최댓값 위치가 지금 위치가 아닐 때에만 교환
                num_list[idx], num_list[i] = num_list[i], num_list[idx]
                swap(num_list, idx + 1, swap_cnt + 1)  # 다음 위치로 이동
                num_list[idx], num_list[i] = num_list[i], num_list[idx]
            else:  # 지금 위치와 동일하면 교환 없이 넘어감
                swap(num_list, idx + 1, swap_cnt)


T = int(input())
for tc in range(1, T + 1):
    numbers, total_swap_cnt = input().split()
    numbers = list(numbers)  # 주어진 string 숫자를 리스트로 변환
    ans = '0' * len(numbers)  # 최종 정답 변수를 가장 작은 수로 초기화
    swap(numbers, 0, 0)
    print(f'#{tc} {ans}')