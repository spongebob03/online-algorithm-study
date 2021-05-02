def solution(genres, plays):
    answer = []
    genreRank = dict()
    songs = [(idx, genre, play) for idx, (genre, play) in enumerate(zip(genres, plays))]
    for idx, genre, play in songs:
        genreRank[genre] = genreRank.get(genre, 0) + play
    songs.sort(reverse=True, key=lambda x: (x[2], -x[0]))
    
    genreRank = sorted(genreRank.items(), reverse=True, key=lambda x: x[1]) 

    for best, play in genreRank:
        count = 0
        for song in songs:
            if song[1] == best and count < 2:
                answer.append(song[0])
                count += 1
    return answer