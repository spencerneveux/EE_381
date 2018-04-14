# -------------------------------
# Spencer Neveux 
# 015043442
# EE 381 
# 2/25/18
# -------------------------------

# Part 1: Simulation of a binomial r.v. 
# The binomial r.v. is the sum of Bernoulli r.v.s
# We'll look at a specific problem
# n = 5, the number of trials 
# x = 3, the number of success
# p = probability of success

# -------------------------------

import random

n = 5
x = 3
p = 0.7

N = 565656 # The number of repititions 

trial = [0] # single zero element list 
trial = trial * n # n element list filled with zeros 

j = 0 # accumulator variable initial value zero.

E = 0 # accumulator fo average. 

for k in range(N): # Outer Loop

	for i in range(n): # Each binomial trial a sum of Bernoulli Trials
		
		r = random.uniform(0, 1)

		if r < p: 
			trial[i] = 1 # success
		else:
			trial[i] = 0 # failure

	s = sum(trial) # equals the number of 1's in trial
	E = E + s # sum of result of all trials

	if s == x:

		j += 1 # recording the number of favorable trials

prob = j / N # probability determined by frequency of results
avg = E / N # average 
print("The probability is:", "{0:.2f}".format(prob)) # output probability 
print("The average is: ", "{0:.2f}".format(avg)) # output average
