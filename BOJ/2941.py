# 2941. 크로아티아 알파벳


word = input()
idx = -1    # 현재 알파벳을 가르키는 인덱스
cnt = 0    # 알파벳 개수

# 알파벳을 하나씩 돌며 무조건 cnt를 1씩 증가시킨다
# 만약 = 또는 - 를 만나면 이는 무조건 크로아티아 알파벳이다
# j를 만나면 앞의 알파벳을 확인해본다
# 크로아티아 알파벳을 발견하면 continue로 아래 cnt 증가 코드를 무시한다
while idx < len(word) - 1:
    idx += 1
    if word[idx] == '=':
        # = 를 만나면 먼저 dz= 인지 확인 후 맞다면 앞의 d, z로 인해
        # cnt가 2 증가되었을 것이므로 cnt를 1 빼준다
        if idx > 1 and word[idx - 2: idx] == 'dz':
            cnt -= 1
        continue
        
    elif word[idx] == '-':
        continue
 
    elif word[idx] == 'j':
        # j 를 만났는데 앞에 l 이나 n 이 있다면 크로아티아 알파벳이다
        if word[idx - 1] == 'l' or word[idx - 1] == 'n':
            continue

    cnt += 1

print(cnt)


'''
1) c=, s=, z= 검사를 dz=보다 먼저 하니 dz=가 d와 z=로 인식되어 수정하였다
2) 알파벳 검사 이후 idx를 증가시키니 continue로 계산 안되는 경우 떄문에 무한반복되어 수정하였다
3) 처음에는 모든 경우의 수를 if 안의 if로 만들어 그 안에서 idx와 cnt를 증가시켰는데
   반복되는 코드가 너무 많아져 이를 줄이기 위해 continue를 이용하였다
'''