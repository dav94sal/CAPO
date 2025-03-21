from api_calls import add_player

def handle_players(players, db_players):
    # Flatten data
    hash_curr_player = {}
    if db_players:
        for player in db_players:
            hash_curr_player[player["strategy"]] = player


    # Check database for existing players
    for player in players:
        # if player does not exist in database:
        if not db_players or player.strategy not in hash_curr_player:
            # make a fetch call to create a new player
            new_player = add_player({
                "strategy": player.strategy
            })
            db_players.append(new_player)

    return db_players
