import random
from player_class import Player
from api_calls import add_player, get_all_players, new_match

tournament_num = 1

def play_round(player1, player2, last_moves):
    # print(last_moves.get(player2, None))
    move1 = player1.make_move(last_moves["player2"])
    move2 = player2.make_move(last_moves["player1"])
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


def simulate_tournament(players, rounds):
    last_moves = {
        "player1": [],
        "player2": [],
    }

    # Repeat tournament 5 times
    match_num = 1

    while match_num <= 5:
        for i in range(len(players)):
            # Players should play a copy of themselves
            for j in range(i, len(players)):
                player1 = players[i]
                player2 = players[j]

                # Get player ids
                flat_players = { player["strategy"]: player["id"] for player in current_players }

                curr_match = new_match({
                    "match_num": match_num,
                    "tournament_num": tournament_num,
                    "player1": flat_players[player1.strategy],
                    "player2": flat_players[player2.strategy],
                })
                # print(curr_match)

                # Each match is n rounds
                for _ in range(rounds):
                    play_round(player1, player2, last_moves)
                    # print([move.to_dict() for move in last_moves])
                # make db call here after each match
                db_match = {
                    match_num,
                    player1,
                    player2,
                }
        match_num += 1


# create players
players = [
    Player('cooperate'),
    Player('defect'),
    Player('tit-for-tat'),
    Player('tit-for-two-tats'),
    Player('random')
]

# get all players in database
current_players = get_all_players()

# Flatten data
hash_curr_player = {}
if current_players:
    for player in current_players:
        hash_curr_player[player["strategy"]] = player


# Check database for existing players
for player in players:
    # if player does not exist in database:
    if not current_players or not hash_curr_player[player.strategy]:
        # make a fetch call to create a new player
        new_player = add_player({
            "strategy": player.strategy
        })
        current_players.append(new_player)

# Each match up lasts approx. 200 rounds
simulate_tournament(players, random.randint(170, 230))

for player in players:
    print(f'{player.strategy} score: {player.score}')
