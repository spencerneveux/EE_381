#----------------------------------------------

# Project 1
# Spencer Neveux
# EE 381 
# 2/3/18

# Reference:
	# Professor de Sulima-Przyborowski wrote this on the board in order 
	# to teach us an example of probability in python. 

# PART 1
#----------------------------------------------

# Calculate summary stats
# The user inputs the list of #

numbers = []

while True:

	try: 

		n = int(input('Enter a whole number: '))
		numbers.append(n)

	except ValueError:

		break

# -----------------------------------------------

# Calculate the mean of the numbers. 

s = sum(numbers)
N = len(numbers)

mean = s / N

print("The mean of the numbers entered is: ",mean)

# ------------------------------------------------

# Calculate the Median.

numbers.sort()

if N % 2 == 0:
	# For an even number of entries
	p1 = N/2
	p2 = N/2 + 1 
	# Cast and shift for python
	p1 = int(p1) - 1
	p2 = int(p2) - 1
	median = (numbers[p1] + numbers[p2]) / 2
	# For an odd number of entries
else: 
	p = (N + 1) / 2
	# Cast and shift for python
	p = int(p) - 1
	median = (numbers[p])

print('The median of the numbers entered is ', median)

# ---------------------------------------------------

# Calculate the mode. 

from collections import Counter

c = Counter(numbers)

mode = c.most_common()

m = mode[0][1]

if m == 1:
	print("There is no mode")
else:
	print("The mode is ",mode[0][0])

# ---------------------------------------------------

# Calculate the standard deviation of numbers entered
import math 

a = 0 # accumulator variable
for x in numbers:
	y = (x - mean) ** 2
	a += y

sigma = math.sqrt(a/N)

print("The standard deviation is ", sigma)

# Part 2 
#----------------------------------------------
# Pseudo-random number generator
# Below are fixed values for the formula
N = 10000 # norm
A = 4857 # adder
M = 8601 # multiplier

a = 0 # accumulator

S = int(input('Enter a non-negative integer for the seed. '))

k = int(input('Enter the number of random numbers wanted. '))

for i in range (1, k+1):
	S = (M * S + A) % N 
	r = S/N
	print(format('%.4f'%r))

	a = a + r

average = a/k

# Part 3
#----------------------------------------------

# Probability Problem
# Three balls in five cans 
# What is the probability they are distinct?

import math

# Random Number Generator
N = 100000 # norm
A = 4857 # adder
M = 8601 # multiplier
S = 0 # seed

Sum = 0 # initialize counter

Can = [0, 0, 0]

K = int(input('Enter the number of experiments. '))

for k in range(K): # Outer loop
	
	for i in range(3):	# Inner Loop
		S = (M * S + A) % N 
		r = S/N # Random numbers on [0, 1)
		Can_Number = math.floor(r * 5 + 1)
		Can[i] = Can_Number

	if ((Can[0] != Can[1])&(Can[1] != Can[2])&(Can[0] != Can[2])):
		Sum += 1
prob = Sum / K

print("The probability of the three balls being in different cans is:", prob)

