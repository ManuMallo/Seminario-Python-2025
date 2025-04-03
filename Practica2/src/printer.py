def print_score (player_stats, i= "final"):
    
    print( f"Ranking ronda {i}:".center(50))
    print("  Nombre    Kills    Assists    Deaths     MVP      Score")
    for name in player_stats:
        print(name.center(10), end="")
        for value in player_stats[name].values():
            print(str(value).center(10), end="")
        print()
    

