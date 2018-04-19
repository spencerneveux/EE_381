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

    plt.bar(x_value_list, probability_list, color="fuchsia")
    plt.show()

# ----------------------------------------
# Hypothesis Statement
# ----------------------------------------
 # H0: p = 50% Ha: p > 50%

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
    minimum = 10
    critical_key_value = 0
    critical_value_list = []
    critical_value_dictionary = {}

    user_input = int(input("Enter the C.V.\n"))

    for y in range(user_input, 18):

        for x in range(y, 18):
            critical_value = nCx(18, x) * (p ** x) * ((1-p) ** (18 - x))
            critical_value_list.append(critical_value)
            # critical_value_dictionary[x] = critical_value
            
        ans = sum(critical_value_list)
        critical_value_dictionary[y] = ans
        print("\nCritical Value: {0} ; Probability: {1:0.3f}".format(y, ans))
        critical_value_list.clear()

    # for key in critical_value_dictionary:
    #     value = critical_value_dictionary[key]
    #     # Find the smallest difference between 0.05 and cv probabilities
    #     if (0.05 - value) < minimum:
    #         print(value)
    #         minimum = value
    #         critical_key_value = key

    # print("\nP((X > C.V.)|(p = 1/2) = 0.05 ~ {0:0.3f} ; C.V. = {1}".format(minimum, critical_key_value))

# ----------------------------------------
# List of p values
# ----------------------------------------
def PValueGenerator():
    p_value_list = []
    for x in range(55, 100, 5):
        p_value_list.append(x/100)

    return p_value_list

# ----------------------------------------
# Binomial Probabilities for P > 0.5
# ----------------------------------------
def PValueProbabilities(p_value_list):
    P = []
    plot_list = []

    for value in p_value_list:

        for x in range(13):
            probability = nCx(18, x) * (value ** x) * ((1 - value) ** (18 - x))
            P.append(probability)

        answer = sum(P)
        print(value, answer)
        plot_list.append(answer)
        P.clear()
    return plot_list

# ----------------------------------------
# Binomial Probabilities for n = 18
# ----------------------------------------
def BinomialProbabilities():
    P = []
    X = []

    value = float(input("pvalue: "))

    for x in range(19):
        probability = nCx(18, x) * (value ** x) * ((1 - value) ** (18 - x))
        P.append(probability)
        X.append(x)

    Graph(X, P)

BinomialProbabilities()
