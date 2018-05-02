# ----------------------
# Spencer Neveux
# EE 381
# 4/25/18
# ----------------------
import matplotlib.pyplot as plot
import math

men = [59.7, 72.9, 41.9, 46.2, 50.3, 43.2]
women = [63.8, 77.8, 44.5, 48.3, 54.0, 43.5]
n = len(men)

# ------------------------------
# Print Main Menu
# ------------------------------
def printMenu():
    print("\n1. Scatter Plot\n2. Computation of r\n3. Hypothesis Test\n4. Regression Line\n5. Quit")

# ------------------------------
# Get User Menu Choice
# ------------------------------
def getMenuChoice():
    user_input = int(input("Choose a function: "))
    return user_input

# ----------------------
# Scatter Plot
# ----------------------
def scatterPlot(x, y):
    figure = plot.figure()
    figure.suptitle("Lab 5", fontsize=14, fontweight="bold")

    axis = figure.add_subplot(111)
    axis.set_xlabel("Men")
    axis.set_ylabel("Women")

    plot.plot(x, y, 'ro')
    plot.axis([40, 80, 40, 80])

    plot.show()

# ----------------------
# Computing r 
# ----------------------
def rComputation(x, y):
    sumX = 0
    sumXX = 0
    sumY = 0
    sumYY = 0
    sumXY = 0
    numerator = 0
    denominator = 0
    r = 0

    # Determine n 
    n = len(x)

    # Loop through x values and sum 
    for x_values in x:
        sumX += x_values

    # Loop through y values and sum
    for y_values in y:
        sumY += y_values

    # Loop through x values and sum x^2
    for x_values in x:
        x_squared = x_values ** 2
        sumXX += x_squared

    # Loop through y values and sum y^2
    for y_values in y:
        y_squared = y_values ** 2
        sumYY += y_squared

    # Loop through both lists and sum the multiplication of values
    for (x, y) in zip(x, y):
        multiplicationXY = x * y
        sumXY += multiplicationXY

    # Calculating Numerator
    numerator = (n * sumXY) - (sumX * sumY)

    # Calculating Denominator
    denominator = math.sqrt(((n * sumXX) - ((sumX) ** 2)) * ((n * sumYY) - ((sumY) ** 2)))
    
    # R calculation
    r = numerator / denominator

    # print("\nThe r value is {0:0.3f}".format(r))
    return r

# ----------------------
# Hypothesis Test
# ----------------------
def hypothesisTest(r):
    c_v = 2.132
    # Determine Test Value
    test_value = r * math.sqrt((n - 2) / (1 - r ** 2))
    print("\nThe test value is {0:.3f}".format(test_value))

    if test_value > c_v:
        print("\nReject null hypothesis")
    else:
        print("\nDon't reject null hypothesis")

# ------------------------------
# Correlation - Least Square Fit
# ------------------------------
def leastSquareFit(x, y):
    a = 0
    b = 0
    n = len(x)
    sumX = 0
    sumXX = 0
    sumY = 0
    sumYY = 0
    sumXY = 0

    # Determine n 
    n = len(x)

    # Loop through x values and sum 
    for x_values in x:
        sumX += x_values

    # Loop through y values and sum
    for y_values in y:
        sumY += y_values

    # Loop through x values and sum x^2
    for x_values in x:
        x_squared = x_values ** 2
        sumXX += x_squared

    # Loop through y values and sum y^2
    for y_values in y:
        y_squared = y_values ** 2
        sumYY += y_squared

    # Loop through both lists and sum the multiplication of values
    for (x, y) in zip(x, y):
        multiplicationXY = x * y
        sumXY += multiplicationXY

    a_numerator = (sumY * sumXX) - (sumX * sumXY)
    a_denominator =  (n * sumXX) - (sumX ** 2)

    b_numerator = (n * sumXY) - (sumX * sumY) 
    b_denominator = (n * sumXX) - (sumX ** 2)

    a = a_numerator / a_denominator
    b = b_numerator / b_denominator
    print("\ny' = {0:.3f}x {1:.3f}".format(b, a))

    # Expected women value for men = 60
    regression_line = (b * 60) + a 
    print("\nThe value for women's life expectancy when men's life expectancy = 60 is {0:.3f}".format(regression_line))

# ------------------------------
# Main
# ------------------------------
def main():
    while True:
        printMenu()
        user_input = getMenuChoice()
    
        if user_input == 1:
            scatterPlot(men, women)
        elif user_input == 2:
            r = rComputation(men, women)
            print("\nThe r value is {0:0.3f}".format(r))
        elif user_input == 3:
            r = rComputation(men, women)
            hypothesisTest(r)
        elif user_input == 4:
            leastSquareFit(men, women) 
        elif user_input == 5:
            print("Ok bye!")
            break 

main()