# 17686. [3차] 파일명 정렬


def solution(files):
    for file_index, file in enumerate(files):
        number_start_index = 0  # 처음 숫자가 시작되는 인덱스
        while not file[number_start_index].isnumeric():
            number_start_index += 1

        number_end_index = number_start_index  # 처음 숫자가 끝나는 인덱스
        while number_end_index < len(file) - 1 and file[number_end_index + 1].isnumeric():
            number_end_index += 1

        # HEAD, NUMBER, 파일의 인덱스, 파일 명을 새로 저장
        files[file_index] = [
            file[0: number_start_index].lower(),
            int(file[number_start_index: number_end_index + 1]),
            file_index,
            file
        ]

    # 파일 정렬 후 파일명만 출력
    files.sort()
    answer = [file[3] for file in files]

    return answer
