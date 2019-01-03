#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author : mao-xu
# date   : 2019/1/3

import gym

env = gym.make("GridGame-v0")
env.reset()
env.render()
env.close()