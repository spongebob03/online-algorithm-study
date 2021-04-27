from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    # song_dict[장르] = [노래의 고유 번호, 재생 횟수]들의 리스트
    song_dict = defaultdict(list)
    for i, (genre, play) in enumerate(zip(genres, plays)):
        song_dict[genre].append([i, play]) 
    
    # genre_dict[장르] = 해당 장르의 총 재생 횟수 
    genre_dict = {}
    for genre in song_dict:
        # album_dict의 각 장르 내에서 재생 횟수가 많은 순으로 정렬 
        song_dict[genre].sort(key=lambda x: x[1], reverse=True)
        genre_dict[genre] = sum([song[1] for song in song_dict[genre]])
    
    # 총 재생 횟수가 많은 장르대로 정렬 
    genre_dict = dict(sorted(genre_dict.items(), key=lambda item: item[1], reverse=True))
    
    # 총 재생 횟수가 많은 장르부터 
    for genre in genre_dict:
        # 각 장르 내에서 재생 횟수가 가장 많은 2개씩 뽑아 해당 노래의 고유번호를 answer에 추가
        answer += [song[0] for song in song_dict[genre][:2]]
    
    return answer