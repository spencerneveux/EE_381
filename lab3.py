#---------------------
# Spencer Neveux
# Lab 3
# EE 381
# 4/5/18
#---------------------
import random
import matplotlib.pyplot as plt 

# Menu options
def print_menu():
    print("\nMain Menu\n1. Part 1\n2. Part 2\n3. Part 3\n4. Quit")

# Get user choice from menu options
def get_menu_choice():
	user_menu_choice = int(input("Choose a function:\n"))
	while not (1 <= user_menu_choice <= 4):
		user_menu_choice = int(input("Not a valid input. Choose a function:\n"))
	return user_menu_choice

# Generate Graph
def graph(list_successes, probability_list):
    # Setting up graph title
    fig = plt.figure()
    fig.suptitle('Lab 3: Part 3', fontsize=14, fontweight='bold')

    # Setting graph labels for title, x axis, y axis
    ax = fig.add_subplot(111)
    fig.subplots_adjust(left=.125, top=0.85)

    ax.set_title('Probability P({X=x})')
    ax.set_xlabel('Success (x values)')
    ax.set_ylabel('Probability')

    # Plotting the graph
    plt.bar(list_successes, probability_list, color="red", edgecolor="black")
    plt.show()

# Print user options for part 3 and act on choice
def print_part_3_choice():
    print("\nWould you like to see a graph?\n")

# Get user choice for part 3
def get_part_3_user_choice(list_successes, probability_list):
    user_choice = input("Enter Y/N: ")
    user_choice = user_choice.lower()
    if user_choice == 'y':
        graph(list_successes, probability_list)
    elif user_choice == 'n':
        print("\nOk, returning to main menu")


# ---------------------
# Part 1 - probability
# ---------------------

def part_1():
    # Constant Variables for part 1
    n = 5
    x = 3
    p = 0.7

    N = 565656

    total_success = 0
    desired_success = 0
    trials = [0]
    trials *= n

    # Outer loop to run through N number of repititions 
    for k in range(N):

        # Inner loop to calculate bernoulli trials
        for i in range(n):
            
            # Generate a random number to determine success or failure
            random_number = random.uniform(0, 1)

            if random_number < p:

                trials[i] = 1 # Success
            
            else:

                trials[i] = 0 # Fail

        # Sum up successful results
        number_success = sum(trials)

        # Sum up all results from N rep.
        total_success += number_success

        if number_success == x: 

            desired_success += 1

    probability = desired_success / N

    print("\nPart 1: The probability is:", "{0:.2f}".format(probability))
    


#----------------------
# Part 2 - average
#------------------------

def part_2():
    # Constant Variables for part 1
    n = 5
    x = 3
    p = 0.7

    N = 565656

    total_success = 0
    trials = [0]
    trials *= n

    # Outer loop to run through N number of repititions 
    for k in range(N):

        # Inner loop to calculate bernoulli trials
        for i in range(n):
            
            # Generate a random number to determine success or failure
            random_number = random.uniform(0, 1)

            if random_number < p:

                trials[i] = 1 # Success
            
            else:

                trials[i] = 0 # Fail

        # Sum up successful results
        number_success = sum(trials)

        # Sum up all results from N rep.
        total_success += number_success

    average = total_success / N

    print("\nPart 2: The average is:", "{0:.2f}".format(average))
    


#-----------------------
# Part 3
#-----------------------

def part_3():

    n = int(input("\nPlease enter the number of trials: ")) # Total number of trials
    x1 = int(input("\nPlease enter the lowest expected number of successes: ")) # desired number of success
    x2 = int(input("\nPlease enter the highest expected number of successes: "))
    p = float(input("\nPlease enter the probability of the event's success: (e.g. .5 for likelihood of heads on fair coin)\n")) # Probability of event occurring


    N = 565656

    total_success = 0
    desired_success = 0
    trials = [0]
    trials *= n
    probability_list = []

    list_successes = list(range(x1, x2+1))

    for j in list_successes:
        # Outer loop to run through N number of repititions 
        for k in range(N):

            # Inner loop to calculate bernoulli trials
            for i in range(n):
                
                # Generate a random number to determine success or failure
                random_number = random.uniform(0, 1)

                if random_number < p:

                    trials[i] = 1 # Success
                
                else:

                    trials[i] = 0 # Fail

            # Sum up successful results
            number_success = sum(trials)

            # Sum up all results from N rep.
            total_success += number_success

            if number_success == j: 

                desired_success += 1

        probability = desired_success / N
        probability_list.append(probability)
        
        average = total_success / N

        desired_success = 0
        total_success = 0

        print("The probability for x = {0} is: {1:.2f} and the average is: {2:.2f}".format(j, probability, average))
        
    return list_successes, probability_list

# Main loop to run program
def main():
    while True:
        print_menu()
        user_choice = get_menu_choice()
        if user_choice == 1:
            part_1()
            continue
        elif user_choice == 2:
            part_2()
            continue
        elif user_choice == 3:
            list_success, probability_list = part_3()
            print_part_3_choice()
            get_part_3_user_choice(list_success, probability_list)
            continue
        elif user_choice == 4:
            print("Ok, bye!")
            break
    
main()