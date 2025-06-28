# I work with Torsten and Etienne
"""
Task: program the simulation in Python, where the agent and the environment are distinct. 
The agent improves its policy by choosing the action according to the Bellman equation.

A state is a pair of numbers, each between 0 and 3 (4x4 grid)
An action is a number 0 - 3
The agent knows its state, and chooses an action. 
The environment returns a reward and a new state
Simulate 1000 steps. Does it converge to the values in Fig 4.1?
"""

import random as rd

# Gridworld size
GRID_SIZE = 4

# Initialize state values
value = {}
visit_count = {}

# Terminal states
terminal_states = [(0, 0), (3, 3)]

# Actions: Left, Up, Right, Down
actions = {
    0: (0, -1),  # Left
    1: (-1, 0),  # Up
    2: (0, 1),   # Right
    3: (1, 0)    # Down
}

# Initialize state values
def init_values():
    global value, visit_count
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            value[(row, col)] = 0  # Start with 0 value
            visit_count[(row, col)] = 0  # Track visits
init_values()

# Reward function
def reward(state):
    if state in terminal_states:
        return 0  # No reward in terminal states
    return -1  # Default reward for all moves

# State transition function
def state_transition(state, action):
    if state in terminal_states:
        return state  # Stay in terminal state
    
    dx, dy = actions[action]
    new_state = (state[0] + dx, state[1] + dy)

    # Check if new state is out of bounds
    if new_state[0] < 0 or new_state[0] >= GRID_SIZE or new_state[1] < 0 or new_state[1] >= GRID_SIZE:
        return state  # Stay in the same state if hitting the boundary
    
    return new_state

# Simulate 1000 steps
for step in range(1000):
    state = (rd.randint(0, 3), rd.randint(0, 3))  # Start at a random non-terminal state
    while state in terminal_states:
        state = (rd.randint(0, 3), rd.randint(0, 3))

    action = rd.randint(0, 3)  # Choose a random action
    new_state = state_transition(state, action)  # Move to new state
    r = reward(state, action)  # Get reward

    # Update visit count
    visit_count[state] += 1
    alpha = 1 / visit_count[state]  # Learning rate

    # Value update formula
    value[state] = (1 - alpha) * value[state] + alpha * (r + value[new_state])

# Print final values to compare with Figure 4.1
for row in range(GRID_SIZE):
    print([round(value[(row, col)], 2) for col in range(GRID_SIZE)])



