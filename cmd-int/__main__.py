import random
from player import Player

def play_round(player1, player2, last_moves):
    # print(last_moves.get(player2, None))
    move1 = player1.make_move(last_moves.get(player2, None))
    move2 = player2.make_move(last_moves)
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
    last_moves[player1] = move1
    last_moves[player2] = move2

def simulate_tournament(players, rounds):
    last_moves = {}
    for _ in range(rounds):
        for i in range(len(players)):
            for j in range(i + 1, len(players)):
                play_round(players[i], players[j], last_moves)
                # print(dict(last_moves))

# Example usage
players = [
    Player('cooperate'),
    Player('defect'),
    Player('tit-for-tat'),
    Player('tit-for-two-tats'),
    Player('random')
]

simulate_tournament(players, random.randint(170, 230))

for player in players:
    print(f'{player.strategy} score: {player.score}')
