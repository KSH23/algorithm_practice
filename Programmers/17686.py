# 17686. [3차] 파일명 정렬


def solution(files):
    for file_index, file in enumerate(files):
        number_start_index = 0  # 처음 숫자가 시작되는 인덱스
        while not file[number_start_index].isnumeric():
            number_start_index += 1

        number_end_index = number_start_index  # 처음 숫자가 끝나는 인덱스
        while number_end_index < len(file) - 1 and file[number_end_index + 1].isnumeric():
            number_end_index += 1

        # HEAD, NUMBER, 기존의 파일 명을 담은 리스트로 교체
        files[file_index] = [
            file[0: number_start_index].lower(),
            int(file[number_start_index: number_end_index + 1]),
            file
        ]

    # 파일 정렬 후 파일명만 출력
    # 파이썬의 sort() 메서드는 안정 정렬을 하기 때문에 정렬시 입력 순서를 유지한다
    files.sort(key = lambda x: (x[0], x[1]))
    answer = [file[2] for file in files]

    return answer
