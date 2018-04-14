# -------------------------------
# Spencer Neveux 
# 015043442
# EE 381 
# 2/25/18

# -------------------------------

# Part 1

import random

print("This section will simulate Bernoulli trials, specifically for coin tosses.")

# Collect user input/validate
prob_success = float(input("\nEnter the probability of success: "))
while not(prob_success >= 0 and prob_success <= 1):
	prob_success = float(input("\nValue must be between 0 and 1. Enter the probability of success: "))

num_trial = int(input("\nEnter the number or trials: "))
while not(num_trial >= 0):
	num_trial = int(input("\nYou must enter an integer greater than zero. Enter the number or trials: "))

trials = [0]
trials *= num_trial # List of specific # trials

# Verify success/failure
for j in range(num_trial):

	random_number = random.uniform(0,1)

	if random_number < prob_success:

		trials[j] = "Sucess" # Success

	elif random_number > prob_success:

		trials[j] = "Failure" # Failure

	print("\nThe results are: " + str(trials[j]))

# ---------------------------

# Part 2
print("\nThis section will calculate Bayes probabilities.")
print("\nC = Probability of having the disease.\nB = Probability of testing positive.\nB'= Probability of a false positive result")

# Lists of assigned values.
prob_disease = [0.0001, 0.001, 0.001, 0.0001, 0.001]
positive = [0.9, 0.9, 0.9, 0.95, 0.95]
false_positive = [0.001, 0.001, 0.01, 0.001, 0.01]

# Loop through list values and calculate Bayes Probabilities
for i in range(5):
	# The probability of having the disease and testing positive
	prob_disease_and_positive = prob_disease[i] * positive[i]

	# The probability of not having the disease and testing positive
	prob_disease_and_false_positive = (1 - prob_disease[i]) * false_positive[i]

	# The probability of having the disease given you tested positive 
	prob_disease_given_positive = (prob_disease_and_positive) / (prob_disease_and_positive + prob_disease_and_false_positive)

	print("\nC =", prob_disease[i], "B =", positive[i], "B' =", false_positive[i], 
		"\nThus, the probability of having the disease given you test positive is:", "{0:.2f}".format(prob_disease_given_positive * 100),"%")
