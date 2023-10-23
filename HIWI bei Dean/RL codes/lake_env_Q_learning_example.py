# Source: https://medium.com/iecse-hashtag/rl-part-5-implementing-an-iterable-q-table-in-python-a9b515c2c1a
# Smilar interesting articles are available under: https://medium.com/@priyambasu16

import numpy as np
import gym
import random
import time
from IPython.display import clear_output



env = gym.make("FrozenLake-v1")
state_space_size = env.observation_space.n
action_space_size = env.action_space.n

#Creating a q-table and intialising all values as 0
q_table = np.zeros((state_space_size,action_space_size))
print(q_table)

#Number of episodes
num_episodes = 10000
#Max number of steps per episode
max_steps_per_episode = 100

learning_rate = 0.1
discount_rate = 0.99

#Greedy strategy
exploration_rate = 1
max_exploration_rate = 1
min_exploration_rate = 0.01
exploration_decay_rate = 0.01

#List to contain all the rewards of all the episodes given to the agent
rewards_all_episodes = [] 


for episode in range(num_episodes): #Contains that happens in an episode
    state = env.reset()[0]
    
    done = False #Tells us whether episode is finished
    rewards_current_episode = 0
    
    for step in range(max_steps_per_episode): #Contains that happens in a time step
        
        #Exploration-exploitation trade off
        exploration_rate_threshold = random.uniform(0,1)
        
        if exploration_rate_threshold > exploration_rate:
            action = np.argmax(q_table[state,:])
        else:
            action = env.action_space.sample()
        
        new_state, reward,_ ,done, info = env.step(action)
        
        #Update Q-table for Q(s,a)
        q_table[state, action] = q_table[state, action] * (1 - learning_rate) + \
            learning_rate * (reward + discount_rate * np.max(q_table[new_state, :]))
            
        state = new_state
        rewards_current_episode += reward
        
        #Checking if episode is over
        if done == True: 
            break
    
    # Exploration rate decay
    exploration_rate = min_exploration_rate + \
        (max_exploration_rate - min_exploration_rate) *\
            np.exp(-exploration_decay_rate*episode)
    
    rewards_all_episodes.append(rewards_current_episode)
    
    
# Calculate and print the average reward per thousand episodes
rewards_per_thousand_episodes = np.split(np.array(rewards_all_episodes),
                                         num_episodes/1000)
count = 1000

print("********Average reward per thousand episodes********\n")
for r in rewards_per_thousand_episodes:
    print(count, ": ", str(sum(r/1000)))
    count += 1000#Print the updates Q-Table
print("\n\n*******Q-Table*******\n")
print(q_table)


for episode in range(5):
    # initialize new episode params
    state = env.reset()
    done = False
    print("*******Episode ", episode+1,"\n",q_table, "*******\n\n\n\n")
    time.sleep(1)



