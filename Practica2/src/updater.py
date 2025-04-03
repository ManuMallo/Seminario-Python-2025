def update_player (total, add, mvp, player):
    """actualiza uno por uno los stats de cada jugador 
       y si su puntaje es mayor al mvp se lo actualiza como nuevo mvp"""
    score=0

    total["kills"] += add["kills"]
    total["assists"] += add["assists"]
    if add["deaths"]:
        total["deaths"] += 1

    score += add["kills"] * 3
    score += add["assists"]
    if add["deaths"]:
        score -= 1
    total["score"] += score

    if score > mvp["score"]:
        mvp["score"] = score
        mvp["player"] = player


def update_stats(player_stats, round):
    """recorre cada jugador llamando a update_player() y al final suma 1
       al mvp del jugador con mayor puntaje"""
    
    mvp = {"player": "", "score": -2}
    for player in round:
        update_player(player_stats[player], round[player],mvp, player)
    player_stats[mvp["player"]]["mvp"] += 1
    return player_stats



            
