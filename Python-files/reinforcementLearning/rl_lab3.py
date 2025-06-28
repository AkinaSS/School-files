"""Task: program the simulation in Python, where the agent and the environment are distinct. 
The agent uses a random policy where there are 4 actions in each state, and they are all equally likely

A state is a pair of numbers, each between 0 and 4
An action is a number 0 - 3
The agent knows its state, and chooses an action. It keeps track of the average reward for 
The environment returns a reward and a new state
Simulate 1000 steps. How well do the averages fit the values in Fig 3.2?
Work in groups and make sure  include the names of the members in your group

gridworld
section 3.5

actions
0 = left
1 = up
2 = right
3 = down

I work with Torsten
"""

import random as rd

state = (0, 0)
value = {}

# the 4 actions the agent can take
actions = {
    0: (0, -1),  # Left
    1: (-1, 0),  # Up
    2: (0, 1),   # Right
    3: (1, 0)    # Down
}

def init_values():
    global value
    for row in range(5):
        for col in range(5):
            value[(row, col)] = (0, 0)  # (total_reward, visit_count)
    return value

def update_average_reward(state, reward):
    global value
    total_reward, visit_count = value[state]
    value[state] = (total_reward + reward, visit_count + 1)

def choose_action():
    return rd.randrange(4)  # 0-3

def reward(action):
    global state
    r = 0  # Default reward for normal states

    # Boundary penalties
    if state[1] == 0 and action == 0: r = -1
    if state[1] == 4 and action == 2: r = -1
    if state[0] == 0 and action == 1: r = -1
    if state[0] == 4 and action == 3: r = -1

    # Special states
    if state == (0, 1):  # State A
        state = (4, 1)
        r = 10
    elif state == (0, 3):  # State B
        state = (2, 3)
        r = 5

    return r

#Moves the agent to a new state based on the chosen action. 
#If the action leads outside the grid, the agent remains in the same state.
def move(action):
    global state
    # Calculate the potential new state
    new_row = state[0] + actions[action][0]
    new_col = state[1] + actions[action][1]

    # Check boundaries (stay in the same state if out of bounds)
    if 0 <= new_row < 5 and 0 <= new_col < 5:
        state = (new_row, new_col)

#Simulates the agent for the given number of steps.
def simulate_steps(steps):
    global state
    total_reward = 0

    for _ in range(steps):
        action = choose_action()  # Random action
        move(action)              # Update state
        r = reward(action)        # Get the reward
        update_average_reward(state, r)  # Track reward for the state
        total_reward += r         # Track total reward

    # Calculate and display average rewards for all states
    print("State values (average rewards):")
    for row in range(5):
        for col in range(5):
            total, count = value[(row, col)]
            avg = total / count if count > 0 else 0
            print(f"State ({row}, {col}): {avg:.2f}")

# Initialize the value dictionary
value = init_values()

# Simulate 1000 steps
simulate_steps(1000)
