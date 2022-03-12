# 17683. [3차] 방금그곡


def make_score(music_info):
    """
    :param music_info: 곡 정보 string
    :return: 각 음을 구분해 저장한 리스트
    """
    score = []  # 곡의 악보

    index = 0
    while index < len(music_info) - 1:
        if music_info[index + 1] == "#":  # 음에 #이 포함된 경우
            score.append(music_info[index: index + 2])
            index += 2
        else:  # 음에 #이 포함되지 않은 경우
            score.append(music_info[index])
            index += 1

    if index == len(music_info) - 1:  # 마지막 음에 #이 포함되지 않아 추가해야 하는 경우
        score.append(music_info[index])

    return score


def make_minutes(time):
    """
    :param time: 시각 string
    :return: 시각을 분으로 변환해 정수화한 값
    """
    hour, minute = map(int, time.split(":"))
    return hour * 60 + minute


def solution(m, musicinfos):
    m = make_score(m)

    played_music = []
    for idx, musicinfo in enumerate(musicinfos):
        start, end, title, score = musicinfo.split(",")
        length = make_minutes(end) - make_minutes(start)  # 재생 길이
        score = make_score(score)  # 재생된 악보

        index, score_index = 0, 0
        while index + score_index < length:
            if len(score) <= index + score_index:  # 곡이 끝났는데 재생 시간이 끝나지 않은 경우 다시 재생
                score += score

            if m[index] == score[index + score_index]:  # 곡의 음이 일치하는 경우
                index += 1
                if index == len(m):
                    # 모든 음이 포함된 경우 정답 후보에 추가 이때 추후 정렬 편의를 위해 길이는 음수로 기록
                    played_music.append((-length, make_minutes(start), title))
                    break

            else:  # 곡의 음이 일치하지 않는 경우
                index = 0
                score_index += 1

    if played_music:
        # 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을,
        # 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환하기 위해 정렬
        played_music.sort(key=lambda x: (x[0], x[1]))
        return played_music[0][2]

    return "(None)"
