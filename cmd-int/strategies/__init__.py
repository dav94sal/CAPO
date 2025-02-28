import strategies.strat_funcs as strat_funcs

strategy_router = {
    "cooperate": lambda _: 'C',
    "defect": lambda _: 'D',
    "tit-for-tat": strat_funcs.tit_for_tat,
    "tit-for-two-tats": strat_funcs.tit_for_two_tats,
    "random": strat_funcs.random_choice
}
