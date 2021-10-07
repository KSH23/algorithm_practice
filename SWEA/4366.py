# 4366. 정식이의 은행업무


T = int(input())
for tc in range(1, T + 1):
    possible_num = set()
    binary = list(input())
    ternary = list(input())

    for idx in range(len(binary)):
        if binary[idx] == '1':
            binary[idx] = '0'
            temp = int(''.join(binary), 2)
            possible_num.add(temp)
            binary[idx] = '1'
        else:
            binary[idx] = '1'
            temp = int(''.join(binary), 2)
            possible_num.add(temp)
            binary[idx] = '0'

    for idx in range(len(ternary)):
        if ternary[idx] == '2':
            ternary[idx] = '0'
            temp = int(''.join(ternary), 3)
            if temp in possible_num:
                break
            ternary[idx] = '1'
            temp = int(''.join(ternary), 3)
            if temp in possible_num:
                break
            ternary[idx] = '2'
        elif ternary[idx] == '1':
            ternary[idx] = '0'
            temp = int(''.join(ternary), 3)
            if temp in possible_num:
                break
            ternary[idx] = '2'
            temp = int(''.join(ternary), 3)
            if temp in possible_num:
                break
            ternary[idx] = '1'
        else:
            ternary[idx] = '1'
            temp = int(''.join(ternary), 3)
            if temp in possible_num:
                break
            ternary[idx] = '2'
            temp = int(''.join(ternary), 3)
            if temp in possible_num:
                break
            ternary[idx] = '0'

    print(f'#{tc} {temp}')