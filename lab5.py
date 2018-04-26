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

# ----------------------
# Scatter Plot
# ----------------------
def scatterPlot(x, y):
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

    print("The r value is {0:0.3f}".format(r))
    return r

# ----------------------
# Hypothesis Test
# ----------------------
def hypothesisTest(r):
    c_v = 2.132
    # Determine Test Value
    test_value = r * math.sqrt((n - 2) / (1 - r ** 2))
    print(test_value)

    if test_value > c_v:
        print("Reject null hypothesis")
    else:
        print("Don't reject null hypothesis")

# ----------------------
# Correlation
# ----------------------



r = rComputation(men, women)
hypothesisTest(r)