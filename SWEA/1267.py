# 1267. 작업순서


# 리스트를 2개씩 짝지은 후 [1] 위치에 등장하는 횟수를 세고
# [0] 위치의 숫자가 결과리스트에 들어있다면 짝인 [1]의 cnt를 하나씩 줄임
# cnt가 0이 되면 결과 리스트에 들어갈 수 있음
# 다시 결과리스트를 돌며 짝궁 [1]의 cnt를 하나씩 줄임

def order(v, e, line_list):
    lines = []

    # line_list에서 숫자를 받아 두 개씩 짝지어 lines에 리스트로 넣음
    for i in range(e):
        lines += [([line_list[2 * i], line_list[2 * i + 1]])]

    cnt = [0] * (v+1)    # 짝지어진 리스트에서 [1] 위치에 몇 번이나 등장하는지 세는 변수
    for i in range(e):
        cnt[lines[i][1]] += 1

    # 처음 들어갈 숫자는 [1] 자리에서 한 번도 호명되지 않았을 것이므로 cnt가 0인 숫자들을 넣음
    first = []
    for i in range(1, v+1):
        if cnt[i] == 0:
            first += [i]
  
    # 최종 결과를 저장할 리스트를 만들고 거기에 위에서 구한 first 값을 넣음
    result_check = []
    result_check += first

    while True:
        if len(result_check) == v:    # 최종 리스트에 모든 숫자가 들어가면 break
            break

        for num in result_check:    # 결과리스트에 있는 숫자들에 대하여
            x = 0
            while x < len(lines):
                line = lines[x]    # 짝지어진 리스트를 하나씩 불러오고
                
                # 만약 결과리스트의 값이 등장하면 그 짝궁 [1]의 cnt를 하나 줄이고
                if line[0] == num and cnt[line[1]] > 0:
                    cnt[line[1]] -= 1
                    lines.remove(line)    # 처리되었으니 삭제
                x += 1

        # cnt를 하나하나 검사하며 0이 된 값이 있는지 확인하고
        # 0이면서 결과리스트에 없다면 결과리스트에 추가함
        for i in range(1, v+1):
            if cnt[i] == 0 and i not in result_check:
                result_check += [i]

    return result_check


T = 10
for tc in range(1, T+1):
    V, E = map(int, input().split())
    my_line_list = list(map(int, input().split()))
    print_ans = " ".join(map(str, order(V, E, my_line_list)))
    print('#{} {}'.format(tc, print_ans))