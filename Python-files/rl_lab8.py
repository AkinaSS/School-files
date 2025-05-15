import random
import numpy as np

class Maze:
    def __init__(self, grid_size, start, goal, obstacles):
        self.grid_size = grid_size
        self.start = start
        self.goal = goal
        self.state = start
        self.obstacles = obstacles  # List of obstacle positions
        self.actions = ['up', 'down', 'left', 'right']
        
    def reset(self):
        self.state = self.start
        return self.state
    
    def is_valid_move(self, row, col):
        # Check if the position is within bounds and not an obstacle
        if 0 <= row < self.grid_size[0] and 0 <= col < self.grid_size[1]:
            if (row, col) in self.obstacles:
                return False  # It's an obstacle
            return True  # Valid move
        return False  # Out of bounds
    
    def step(self, action):
        row, col = self.state
        
        # Try to move based on action
        if action == 'up':
            new_row, new_col = row - 1, col
        elif action == 'down':
            new_row, new_col = row + 1, col
        elif action == 'left':
            new_row, new_col = row, col - 1
        elif action == 'right':
            new_row, new_col = row, col + 1
        
        # Check if the move is valid (not out of bounds or into an obstacle)
        if self.is_valid_move(new_row, new_col):
            self.state = (new_row, new_col)
        else:
            # If not a valid move, stay in the same position
            new_row, new_col = row, col
        
        # Reward function
        if (new_row, new_col) == self.goal:
            reward = 1  # Goal state reward
        else:
            reward = -0.5
        
        return (new_row, new_col), reward
    
    def is_done(self):
        return self.state == self.goal


class DynaQAgent:
    def __init__(self, maze, alpha=0.1, gamma=0.9, epsilon=0.1, n_planning=10):
        self.maze = maze
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.n_planning = n_planning
        self.q_values = np.zeros((maze.grid_size[0], maze.grid_size[1], len(maze.actions)))
        self.model = {}  # Model will store (state, action) -> (next_state, reward)
        
    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.maze.actions)  # Exploration
        else:
            state_row, state_col = state
            action_values = self.q_values[state_row, state_col, :]
            return self.maze.actions[np.argmax(action_values)]  # Exploitation
    
    def learn(self, state, action, reward, next_state):
        state_row, state_col = state
        action_idx = self.maze.actions.index(action)
        next_state_row, next_state_col = next_state
        
        # Update Q-values based on the real experience
        best_next_action_value = np.max(self.q_values[next_state_row, next_state_col, :])
        self.q_values[state_row, state_col, action_idx] += self.alpha * (
            reward + self.gamma * best_next_action_value - self.q_values[state_row, state_col, action_idx]
        )
        
        # Update the model
        self.model[(state, action)] = (next_state, reward)
    
    def planning_step(self):
        # Planning: simulate experiences using the model
        for _ in range(self.n_planning):
            (state, action), (next_state, reward) = random.choice(list(self.model.items()))
            self.learn(state, action, reward, next_state)

def run_dyna_q(maze, agent, episodes=1000):
    total_rewards = []
    
    for episode in range(episodes):
        state = maze.reset()
        total_reward = 0
        
        while not maze.is_done():
            action = agent.choose_action(state)
            next_state, reward = maze.step(action)
            
            # Update the agent's Q-values based on the real experience
            agent.learn(state, action, reward, next_state)
            
            # Planning step: use the model to simulate experiences
            agent.planning_step()
            
            state = next_state
            total_reward += reward
        
        total_rewards.append(total_reward)
        print(f"Episode {episode + 1}, Total Reward: {total_reward}")
    
    return total_rewards

# Define the maze and agent parameters
grid_size = (9, 6)  # 5x5 maze
start = (0, 2)  # Starting position
goal = (8, 0)   # Goal position

# Define obstacles as a list of positions (row, col)
obstacles = [(2,1),(2,2),(2,3),(5,4),(7,0),(7,1),(7,2)]  # Obstacles in the maze

# Create the maze environment and agent
maze = Maze(grid_size, start, goal, obstacles)
agent = DynaQAgent(maze)

# Run Dyna-Q on the maze
total_rewards = run_dyna_q(maze, agent)
