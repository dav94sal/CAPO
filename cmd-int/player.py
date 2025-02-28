from strategies import strategy_router

class Player:
    def __init__(self, strategy):
        self.strategy = strategy
        self.score = 0

    def make_move(self, opp_last_moves):
        return strategy_router[self.strategy](opp_last_moves)
