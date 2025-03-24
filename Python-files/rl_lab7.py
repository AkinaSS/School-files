import random as rd

state = (0, 0)
goal_state = (6,3)
starting_state = (0,3)
value = {}
wind_strength = {  
        0: 0, 
        1: 0, 
        2: 0, 
        3: 1, 
        4: 1, 
        5: 1, 
        6: 2, 
        7: 2, 
        8: 1,
        9: 0   }

# the 4 actions the agent can take
actions = {
    0: (0, -1),  # Left
    1: (-1, 0),  # Up
    2: (0, 1),   # Right
    3: (1, 0)    # Down
}

# Discount factor and learning rate
gamma = 0.9  # Discount factor
alpha = 0.1  # Learning rate

# Builds the 7 x 10 grid
def init_values(): 
    global value
    for row in range(7):
        for col in range(10):
            value[(row, col)] = 0  # Initialize all state values to 0
    return value

def choose_action():
    return rd.randrange(4)  # Random action for now (improves later with policy)

def reward(state):
    return 0 if state == goal_state else -1  # -1 penalty for every step

def move(state, action):
    row, col = state
    row_change, col_change = actions[action]

    new_row = row + row_change
    new_col = col + col_change

    # Ensure new_col is within bounds BEFORE applying wind
    new_col = max(0, min(9, new_col))

    # Apply wind effect
    randnum = rd.randint(0, 1)
    
    if randnum == 1:
        new_row -= wind_strength[new_col]

    # Ensure new_row and new_col stay within bounds
    new_row = max(0, min(6, new_row))
    new_col = max(0, min(9, new_col))

    return (new_row, new_col)

def run_td0(num_episodes=500):
    init_values()  # Reset values
    
    for episode in range(num_episodes):
        current_state = starting_state
        steps = 0

        while current_state != goal_state and steps < 1000:
            action = choose_action()  # Pick an action
            new_state = move(current_state, action)  # Get new state
            r = reward(new_state)  # Get reward for new state

            # TD(0) Update Rule
            value[current_state] += alpha * (r + gamma * value[new_state] - value[current_state])

            current_state = new_state  # Move to next state
            steps += 1

        print(f"Episode {episode+1} finished in {steps} steps.")

    return value  # Return the learned value function

# Run TD(0) learning
learned_values = run_td0(num_episodes=500)

# Print final values for inspection
print("\nFinal State Values:")
for row in range(7):
    for col in range(10):
        print(f"V({(row, col)}) = {learned_values[(row, col)]:.2f}", end="\t")
    print()  # New line for each row
