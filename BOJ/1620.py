# 1620. 나는야 포켓몬 마스터 이다솜


import sys


N, M = map(int, sys.stdin.readline().split())

pokemon_dict = {}    # {포켓몬 이름: 포켓몬 번호} 저장
pokemon_list = []    # [포켓몬 이름] 저장, 인덱스가 포켓몬 번호
for pokemon_num in range(1, N + 1):
    pokemon_name = sys.stdin.readline().rstrip()
    pokemon_dict[pokemon_name] = pokemon_num
    pokemon_list.append(pokemon_name)

for _ in range(M):
    quiz = sys.stdin.readline().rstrip()
    if quiz.isdigit():    # 숫자인 경우 인덱스로 호출
        print(pokemon_list[int(quiz) - 1])
    else:    # 이름인 경우 key로 호출
        print(pokemon_dict[quiz])