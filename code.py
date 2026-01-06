pip install gymnasium

import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human") # creating the cartpole environment
state, info = env.reset() # starting a new game


for step in range(500):
    action = env.action_space.sample() # 0: move left and 1: move right 
    state, reward, terminated, truncated, info = env.step(action)
    
    # if pole falls then episode ends 
    if terminated or truncated:
        print("Game Over at step:", step)
        state, info = env.reset()

env.close() # Closing the environment window 
