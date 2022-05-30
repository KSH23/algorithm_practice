# 42579. 베스트앨범


from collections import defaultdict
import heapq


def solution(genres, plays):
    # 장르를 key, 재생 횟수를 value로 기록
    genres_count = defaultdict(int)

    # 장르를 key, 가장 많이 재생된 노래를 (고유 번호, 재생 횟수)로 기록
    genres_songs = defaultdict(lambda: [(-1, -1), (-1, -1)])

    for song in range(len(genres)):
        genre, play = genres[song], plays[song]

        genres_count[genre] += play  # 재생 횟수 갱신

        # 가장 많이 재생된 노래 갱신
        genre_first_song, genre_second_song = genres_songs[genre]
        if genre_first_song[1] < play:  # 가장 많이 재생된 노래보다 많이 재생된 경우
            genres_songs[genre][1] = genres_songs[genre][0]
            genres_songs[genre][0] = (song, play)
        elif genre_second_song[1] < play:  # 두 번째로 많이 재생된 노래보다 많이 재생된 경우
            genres_songs[genre][1] = (song, play)

    counts = []  # 장르별 재생 횟수를 최대힙에 기록
    for genre, count in genres_count.items():
        heapq.heappush(counts, (-count, genre))

    ret = []
    while counts:
        genre = heapq.heappop(counts)[1]

        # 가장 많이 재생된 노래와 존재한다면, 두 번째로 많이 재생된 노래 추가
        first_song, second_song = genres_songs[genre]
        ret.append(first_song[0])
        if -1 < second_song[0]:
            ret.append(second_song[0])

    return ret


print(solution(["a", "b", "c", "d", "a", "d", "d", "d", "a", "a", "c", "c"], [100, 300, 400, 150, 100, 300, 200, 600, 700, 110, 900, 9000]))
