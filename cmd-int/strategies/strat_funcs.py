import random

def tit_for_tat(opp_last_moves):
    return opp_last_moves[-1] if opp_last_moves[-1] else 'C'

def tit_for_two_tats(opp_last_moves):
    # print(opp_last_moves)
    if opp_last_moves[-1] == 'D' and opp_last_moves[-2] == 'D':
        return 'D'
    else:
        return 'C'

def random_choice(_):
    return random.choice(['C', 'D'])
