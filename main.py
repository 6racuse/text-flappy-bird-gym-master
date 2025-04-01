import random
import numpy as np
import gymnasium as gym
from collections import defaultdict

if __name__ == '__main__':
    num_episodes = 1000  # nombre d'épisodes d'entraînement
    shaping_coef = 0.1   # coefficient de reward shaping pour pénaliser |y|
    env = gym.make('TextFlappyBird-v0', height=15, width=20, pipe_gap=4)
    agent = ...
    scores = []

    # Phase d'entraînement
    for episode in range(num_episodes):
        state, info = env.reset()
        done = False
        episode_reward = 0
        while not done:
            action = agent.policy(state)
            next_state, reward, done, _, info = env.step(action)
            state = next_state
    env.close()
