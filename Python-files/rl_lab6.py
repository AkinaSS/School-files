# Blackjack Monte Carlo method example
# for the tuple: 
# first element is player total
# second element is dealer total
# Third element is dealers up card
# 4th is usable ace
# Work with Torsten

import random as rd

ace = 1
num_episodes = 10000  # Number of simulations for Monte Carlo evaluation
state_values = {}  # Dictionary to store average rewards per state

def Choose_Enviroment():
    """Initialize a random blackjack state (player total, dealer total, dealer upcard, usable ace)."""
    player = rd.randint(2, 21)
    dealer = rd.randint(11, 21)
    d_upcard = rd.randint(ace, 11)
    useable_ace = rd.randint(0, 1)

    return (player, dealer, d_upcard, useable_ace)

def policy(player_total):
    """Player policy: hit until reaching 20 or more."""
    while player_total < 20:
        player_total += rd.randint(1, 10)
    return player_total

def dealer_policy(dealer_total):
    """Dealer hits until reaching at least 17 (standard blackjack rule)."""
    while dealer_total < 17:
        dealer_total += rd.randint(1, 10)
    return dealer_total
    
def reward(player, dealer):
    """Returns the reward for the game outcome."""
    if player > 21:
        return -1  # Player busts
    if dealer > 21:
        return 1  # Dealer busts
    if player > dealer:
        return 1  # Player wins
    if player < dealer:
        return -1  # Dealer wins
    return 0  # Tie 


def monte_carlo_evaluation():
    """Runs multiple episodes to evaluate the policy and estimate state values."""
    for _ in range(num_episodes):
        state = Choose_Enviroment()
        player_total, dealer_total, d_upcard, useable_ace = state

        player_total = policy(player_total)
        dealer_total = dealer_policy(dealer_total)
        r = reward(player_total, dealer_total)

        if state in state_values:
            state_values[state].append(r)
        else:
            state_values[state] = [r]

    # Compute average reward for each state
    for state in state_values:
        state_values[state] = sum(state_values[state]) / len(state_values[state])

# Run Monte Carlo evaluation
monte_carlo_evaluation()

# Print some evaluated state values
for k, v in list(state_values.items())[:1000]:  # Show only the first 10 states
    print(f"State {k}: Estimated Value {v:.2f}")


