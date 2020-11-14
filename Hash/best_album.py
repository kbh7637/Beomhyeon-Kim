# https://programmers.co.kr/learn/courses/30/lessons/42579
import collections

genres = ['classic', 'classic', 'pop', 'classic']
plays = [5,5,6,5]
indices = range(len(genres))

def solution(genres, plays):
    answer = []
    indices = range(len(genres))
    album = list(zip(genres, plays, indices))

    hash_map = {}
    for genre, play, idx in album:
        if genre in hash_map:
            hash_map[genre] += play
        else:
            hash_map[genre] = play

    genre_orders = [key for key, value in sorted(hash_map.items(), key = (lambda x : x[1]), reverse = True)] # 장르 합이 큰 순서

    album = sorted(album, key = lambda x : (x[0], -x[1], x[2]))

    hash_num = {}
    answer = []
    for genre_order in genre_orders:
        for genre, play, idx in album:
            if genre_order == genre:
                if genre in hash_num:
                    hash_num[genre] += 1
                    answer.append(idx)
                    if hash_num[genre] == 2:
                        break
                else:
                    hash_num[genre] = 1
                    answer.append(idx)
    return answer