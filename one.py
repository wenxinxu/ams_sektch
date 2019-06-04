#!/usr/bin/env python3
import numpy as np 
import funcs 
import argparse 
import os



#load factor: 1.038
def gaussian_run(iterations, project): 
    m = int(1e4)
    sigma  = 7e3
    k=4
    lambd = 0.1
    epsilon = 0.1


    for _ in range(iterations):
        stream = funcs.stream_distribution('gaussian', m, param1=0, param2=sigma)
        output_error(stream, k, lambd, epsilon, project)


#load factor: 1.075
def uniform_run(iterations, project):
    high =  8.6e3
    m = int(high*100)
    k=4
    lambd = 0.1
    epsilon = 0.1

    for _ in range(iterations):
        stream = funcs.stream_distribution('uniform', m, param1=high)
        output_error(stream, k, lambd, epsilon, project)

#load factor: 1.075
def zipf_run(iterations, project):
    m = int(1e5)
    zipf_param = 1.32
    k=4
    lambd = 0.1
    epsilon = 0.1

    for _ in range(iterations):
        stream = funcs.stream_distribution('zipf', m, param1=zipf_param)
        output_error(stream, k, lambd, epsilon, project)



parser = argparse.ArgumentParser(description='Run simulations and choose parameters.')
parser.add_argument('--iterations', type=int, default=1)
parser.add_argument('--project', type=str, default=None)
parser.add_argument('--distribution', type=str, default=None)
args = parser.parse_args()

assert args.project is not None, "Forgot project name to save results in."
assert args.iterations >= 1, "Num iterations must be > 1"
assert args.distribution is not None, "Distribution must be specified"
if not os.path.isdir(args.project):
    os.mkdir(args.project) 


if args.distribution == 'gaussian':
    gaussian_run(args.iterations, args.project)

elif args.distribution == 'uniform':
    uniform_run(args.iterations, args.project)

elif args.distribution == 'zipf':
    zipf_run(iterations, project)

else: 
    raise NotImplementedError()


