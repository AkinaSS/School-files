# Blackjack Monte Carlo method example
# for the tuple: 
# first element is player total
# second element is dealer total
# Third element is dealers up card
# 4th is usable ace

import random as rd
ace = 1

def Choose_Enviroment():
    player = rd.randint(2,21)
    dealer = rd.randint(11,21)
    d_upcard = rd.randint(ace,11)
    useable_ace = rd.randint(0,1)

    env_state = (player, dealer, d_upcard, useable_ace)
    return env_state

def policy(player, d_upcard, usable_ace):
    stick = "stick" 
    hit = "hit"
    if player >= 21:
        stick
    if player <= 19:
        hit
    

def reward(state):
    r = 0
    player_total = state[0]
    dealer = state[1]

    if player_total > dealer:
        print(player_total)
        print(dealer)
        r = 1
    if player_total < dealer: 
        print(player_total)
        print(dealer)
        r = -1
    if player_total == dealer:
        print(player_total)
        print(dealer)
        r = 0
    return r


new_state = Choose_Enviroment()

print(new_state)
print(reward(new_state))
