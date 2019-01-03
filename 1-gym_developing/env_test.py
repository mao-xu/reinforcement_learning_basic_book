import gym
env = gym.make("GridGame-v0")
env.reset()
env.render()
env.close()