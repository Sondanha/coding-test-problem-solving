# def solution(players, callings):
    
#     for i in callings:
#         n = players.index(i)
#         players[n-1], players[n] = players[n], players[n-1]

#     return players

def solution(players, callings):
    
    player_key_dict = {s:i for i, s in enumerate(players)} # 이름 key 
    rank_key_dict = {i:s for i, s in enumerate(players)}   # 등수 key

    for player in callings:
        
        n = player_key_dict[player]       # 현재 선수의 등수
        front_player = rank_key_dict[n-1] # 앞 선수의 이름
        
        # 등수 바꾸기
        player_key_dict[player] = n-1
        player_key_dict[front_player] = n
        
        # 이름 바꾸기
        rank_key_dict[n] = front_player
        rank_key_dict[n-1] = player
    
    player_list = sorted(player_key_dict.items(), key=lambda x: x[1])
    answer = [i[0] for i in player_list]
    
    return answer
