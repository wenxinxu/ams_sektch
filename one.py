#!/usr/bin/env python3
import numpy as np 
import funcs 
import os

import argparse 
parser = argparse.ArgumentParser(description='Run simulations and choose parameters.')
parser.add_argument('--iterations', type=int, default=1)
parser.add_argument('--project', type=str, default=None)
args = parser.parse_args()

assert args.project is not None, "Forgot project name to save results in."
assert args.iterations >= 1, "Num iterations must be > 1"

m = int(1e4)
sigma  = 7e3
k=2
lambd = 0.1
epsilon = 0.1

for _ in range(args.iterations):
    idx = np.random.randint(1,1e12)
    filename = os.path.join(args.project, f"{idx}.result")
    stream = funcs.stream_distribution('gaussian', m, param1=0, param2=sigma)
    n = funcs.get_frequency_vector(stream).shape[0]
    s1,s2 = funcs.get_s1_s2(n, 2, lambd, epsilon, 'ams')
    ams = funcs.AMS_offline(stream, lambd, epsilon, 'poly', {'k':2})
    estimate = ams.estimate_F2()
    print(estimate, file=open(filename, 'w'))
    print(ams.get_truth(), file=open(filename, 'a'))


# print('load factor: ', n/(s1*s2))

