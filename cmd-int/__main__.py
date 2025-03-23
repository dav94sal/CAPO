import random
from player_data import Player
from api_calls import new_match, get_tourny_num, match_rounds, handle_players, get_all_players
from strategies import strategy_router

tournament_num = get_tourny_num() or 1
print("Tournament num: ", tournament_num)

def play_round(player1, player2, last_moves):
    move1 = player1.make_move(last_moves["player2"])
    move2 = player2.make_move(last_moves["player1"])

    curr_round = {
        "move1": move1,
        "move2": move2
    }

    if move1 == 'C' and move2 == 'C':
        player1.score += 3
        player2.score += 3
    elif move1 == 'C' and move2 == 'D':
        player1.score += 0
        player2.score += 5
    elif move1 == 'D' and move2 == 'C':
        player1.score += 5
        player2.score += 0
    elif move1 == 'D' and move2 == 'D':
        player1.score += 1
        player2.score += 1
    last_moves["player1"].append(move1)
    last_moves["player2"].append(move2)

    return curr_round


def simulate_tournament(players, rounds):
    last_moves = {
        "player1": [],
        "player2": [],
    }

    match_num = 1

    # Repeat tournament 5 times
    while match_num <= 5:
        for i in range(len(players)):
            # Players should play a copy of themselves
            for j in range(i, len(players)):
                player1 = players[i]
                player2 = players[j]

                # Get player ids
                flat_players = { player["strategy"]: player["id"] for player in db_players }

                curr_match = new_match({
                    "match_num": match_num,
                    "tournament_num": tournament_num,
                    "player1": flat_players[player1.strategy],
                    "player2": flat_players[player2.strategy],
                })
                # print(curr_match)

                new_rounds = {}

                # Each match is n rounds
                # Optimization: Group rounds by match, send in batches to backend
                for round in range(rounds):
                    curr_round = play_round(player1, player2, last_moves)
                    curr_round["round"] = round
                    curr_round["match_id"] = curr_match["id"]
                    new_rounds[round] = curr_round

                match_rounds(new_rounds)

        match_num += 1


# create players
# get all players in database
db_players = get_all_players()
players = [Player(strat) for strat in strategy_router]

# Add players to database
db_players = handle_players(players, db_players)

# Each match up lasts approx. 200 rounds
simulate_tournament(players, random.randint(170, 230))

for player in players:
    print(f'{player.strategy} score: {player.score}')
