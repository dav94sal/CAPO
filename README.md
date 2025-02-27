# CAPO

Conflict Analysis Pervasive Objectivity

**Not Complete!!**
-

CAPO is my version of a computer tournament created by Robert Axelrod. I will be creating my own interpretation of the game as well as the strategies known as Tit For Tat, Friedman, Joss, as well as the Sample and Random strategies created by Axelrod.

This simulation is modeled after Rand Corporation's game that has come to be known as The Prisoner's Dilemma and Veritasium, Inc's video essay on [What Game Theory Reveals About Life, The Universe, and Everything](https://www.youtube.com/watch?v=mScpHTIi-kM). The Prisoner's Dilemma closely resembled the Cold war conflict between Russia and the USA

The Prisoner's Dilemma describes a situation where "whatever the other [prisoner] does, each is better off confessing than remaining silent. But the outcome obtained when both confess is worse for each than the outcome they would have obtained had both remained silent." - Stanford Encyclopedia of Philosophy

## The Game

In our game, we follow Dr. Derek Muller's description, restructured for the purposes of this simulation game:

A banker with a chest full of coins invites you to compete in a simple game with a simple goal: obtain as many coins as you can.

- You must compete with another player.
- Both players will be given a choice
    - Cooperate
        - If both players cooperate, both get 3 coins
        - If one player cooperates and one defects, cooperator gets 0 coins,  defector gets 5 coins
    - Defect
        - If both players defect, each get 1 coin
        - If one player defects and one cooperates, defector gets 5 coins, cooperator gets 0 coins


- Tit for tat
- Game Theory

## The Strategies

### Tit For Tat
- Start by cooperating
- Follow oppenents moves, but only once

### Friedman
- Start by Cooperating
- If oppenent Defects only once, defect indefinitely

### Joss
- Start by cooperating
- Copy oppenents moves
- Defect about 10% of rounds

### Sample
- Start by Cooperating
- Only defect if oppenent defects twice in a row

## Best Strategy Qualities

**Nice** - Not being first to defect. (Opposed by **Nasty** - Defects first)

**Forgiving** - Retaliates but doesn't hold a grudge. (Opposed by **Unforgiving** - Holds a grudge)

**Retaliatory** - "If your oppenent defects, strike back immediately. Don't be a pushover." - Veritasium

**Clear** - Programs with a clear stategy perform better than ones that are closer to being random.

## Citations

- [What Game Theory Reveals About Life, The Universe, and Everything](https://www.youtube.com/watch?v=mScpHTIi-kM) - [Veritasium](https://www.veritasium.com/about)

- [Prisoner's Dilemma](https://plato.stanford.edu/entries/prisoner-dilemma/#:~:text=The%20%E2%80%9Cdilemma%E2%80%9D%20faced%20by%20the,obtained%20had%20both%20remained%20silent.) - [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/index.html)
