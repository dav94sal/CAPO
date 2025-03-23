from .strat_funcs import tit_for_tat, tit_for_two_tats, random_choice

strategy_router = {
    "cooperate": lambda _: 'C',
    "defect": lambda _: 'D',
    "tit-for-tat": tit_for_tat,
    "tit-for-two-tats": tit_for_two_tats,
    "random": random_choice,
}
