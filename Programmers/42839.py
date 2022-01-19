# 42839. 소수 찾기


def solution(numbers):
    # 문제의 조건에 따라 numbers가 만들 수 있는 가장 큰 수는 10 ** len(numbers))이며
    # 10 ** len(numbers)) 까지의 소수를 에라스토테네스의 체로 판별
    prime_numbers = [True] * (10 ** len(numbers))
    prime_numbers[0] = prime_numbers[1] = False  # 0과 1은 소수가 아님
    
    # 에라스토테네스의 체
    for num in range(2, int(((10 ** len(numbers)) ** 0.5))):
        if not prime_numbers[num]:
            continue
        for next_num in range(num * 2, len(prime_numbers), num):
            prime_numbers[next_num] = False

    num_list = []  # numbers로 만들 수 있는 모든 경우의 수를 담는 리스트
    for idx in range(len(numbers)):
        # 초깃값을 사용한 숫자 기록용 비트 마스킹과 함께 추가
        num_list.append([numbers[idx], 1 << idx])

    made_num_set = set()  # 만든 소수 저장 세트
    while num_list:
        # 현재 만들어진 숫자와 사용한 숫자를 기록하는 비트 마스킹
        cur_num, bit_mask = num_list.pop()
        
        # 현재 만들어진 숫자가 소수인 경우 세트에 추가
        if prime_numbers[int(cur_num)]:
            made_num_set.add(int(cur_num))
        
        # 사용하지 않은 숫자를 뒤에 붙여 다시 리스트에 추가
        for idx in range(len(numbers)):
            if (1 << idx) & bit_mask:
                continue
            num_list.append([cur_num + numbers[idx], (1 << idx) | bit_mask])

    answer = len(made_num_set)
    return answer