# ----------------
# Spencer Neveux
# EE 381
# 4/17/18
# Project 4 
# --------------

# ----------------------------------------
# Title - Hypothesis Testing
# ----------------------------------------

# Importing and setting up variables
import matplotlib.pyplot as plt 
import numpy as np 
import math 

number_trials = 18
p = 0.5

# ----------------------------------------
# Combinations Calculation
# ----------------------------------------
def nCx(n, x):
    factorial = math.factorial
    return (factorial(n) // (factorial(x) * factorial(n - x)))

# ----------------------------------------
# Generate Graph
# ----------------------------------------
def Graph(x_value_list, probability_list):
    # Setting Up Figure
    fig = plt.figure()
    fig.suptitle("Lab 4: Hypothesis Testing")

    # Set up labels
    ax = fig.add_subplot(111)
    fig.subplots_adjust(left=.125, top=0.85)

    ax.set_title("Probability({X = x})")
    ax.set_xlabel("R.V. values")
    ax.set_ylabel("Probability")

    plt.bar(x_value_list, probability_list)
    plt.show()

# ----------------------------------------
# Hypothesis Statement
# ----------------------------------------
 # H0 = 50% Ha > 50%

# ----------------------------------------
# Binomial Distribution
# ----------------------------------------
def BinomialDist():
    probability_list = []
    x_value_list = list(range(0, 19))

    for x_values in x_value_list:
        probability_x = nCx(18, x_values) * (p ** x_values) * ((1-p) ** (number_trials - x_values))
        probability_list.append(probability_x)

    return x_value_list, probability_list

# ----------------------------------------
# Critical Value
# ----------------------------------------
def CriticalValue():
    user_input = int(input("Enter the C.V.\n"))

    for x in range(user_input, 18):
        critical_value = nCx(18, x) * (p ** x) * ((1-p) ** (18 - x))
        print("Critical Value: {0} ; Probability: {1:0.3f}".format(x, critical_value))

# ----------------------------------------
# List of p values
# ----------------------------------------
p_value_list = []
for x in range(55, 100, 5):
    p_value_list.append(x/100)

print(p_value_list)