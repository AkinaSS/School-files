import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

e = random.random()
steps = 3000
ave_reward = 0

estimated_values = []
for _ in range(10):
    estimated_values.append(random.gauss(0, 1))
    #estimated_values.append(0)

bandits = []
#i is needed to index the estimated_values list
for i in range(10):
    bandits.append([i, random.gauss(0, 1), 1])

counts = []
for _ in range(10):
    counts.append(1)

df = pd.DataFrame(columns=['steps', 'ave_value'])
#print(*estimated_values, sep='\n')

for i in range(steps):
    #epsilon-greedy
    #rand_num = random.randint(0, 100)
    if e <= 0.1: 
        #choose a random bandit from the list
        rand_bandit = random.choice(bandits)
        
        #the reward obtained from pulling that lever
        reward = random.gauss(rand_bandit[1], 1)
        
        #the index of the bandit that is tied to estimated_values list
        index = rand_bandit[0]
        
        # if i == 1:
        #     estimated_values[index] = reward
            
        #new_bandit is the updated estimated value of that lever
        new_est = estimated_values[index] + (1/rand_bandit[2])*(reward - estimated_values[index])
        
        #actually update the value for that lever's estimate (index)
        estimated_values[index] = new_est
        
        #increment counter for given bandit
        rand_bandit[2] += 1
        
        ave_reward = ((ave_reward * (i + 1)) + reward)/(i + 2)
        df.loc[i] = [i, ave_reward]
    else:
        bandit_means = []
        for mean in bandits:
            bandit_means.append(mean[1])
            
        # argmax returns an INDEX
        #index is the index of the largest bandit
        index = np.argmax(bandit_means)
        reward = random.gauss(bandits[index][1], 1)
        
        # if i == 1:
        #     estimated_values[index] = reward
        
        new_est = estimated_values[index] + (1/bandits[index][2])*(reward - estimated_values[index])
        estimated_values[index] = new_est
        bandits[index][2] += 1
        ave_reward = ((ave_reward * (i + 1)) + reward)/(i + 2)
        df.loc[i] = [i, ave_reward]

print(*estimated_values, sep='\n')

est_ave = 0
for est in estimated_values:
    est_ave += est

est_ave = est_ave/10
print(est_ave)

print(*bandits, sep='\n')

true_ave = 0
for bandit in bandits:
    true_ave += bandit[1]

true_ave = true_ave/10
print(true_ave)

#enabled these if you use jupiter notebook
#plt.plot(df['steps'], df['ave_value'])
#plt.show()