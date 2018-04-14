"""
Created on Tue Feb 20 10:25:50 2018
@author: denmcca
"""

import random

def BernoulliTrialSim():
    pass

def RandomCoinToss(headsProb):
    if random.uniform(0,1) < headsProb:
        return 1
    return 0

def GetHeadsProbability():
    return float(input('Enter the probability of flipping Heads: '))

def GetNumberOfTrials():
    return int(input('Enter number of trials to run: '))

def PrintHeadsOrTails(result):
    if result is 1:
        print('Heads')
        return
    print('Tails')

def PerformBaysianCalculation(C, BgivenC, BgivenNotC):
    return (C * BgivenC) / ((1 - C) * BgivenNotC + C * BgivenC)

def PrintBayesianProbability(ProbIn):
    print('\nC|B is {:.7f} or {:.4}%'.format(ProbIn, ProbIn * 100))    

def CoinFlipSimulator():
    print('\nIn this section we will simulate the probability of coin flips')
    input('Press enter to proceed. ')
    
    while True:
        headProb = GetHeadsProbability()
        numTrials = GetNumberOfTrials()
        
        trials = [0];
        trials = trials*numTrials
        heads = 0
        
        for i in range(len(trials)):
            trials[i] = RandomCoinToss(headProb)
            if trials[i] is 1:
                heads += 1
            PrintHeadsOrTails(trials[i])
        
        print('\nHeads was flipped {} out of {} times. A rate of {}.'.format(heads, numTrials, heads/numTrials))
        print('You entered {} as the probability. '.format(headProb))
        if input('Repeat section(y/n)? ') is not 'y':
            break
    
def CalculateBayesProbability():
    print('\nIn this section we will calculate the Bayesian value using the theorem.')
    input('Press enter to proceed. ')
    while True:
        while True:    
            try:
                C = float(input('Enter probability of C: '))
                break
            except:
                print('Invalid input detected -- try again!')
        
        while True:
            try:
                BgivenC = float(input('Enter probability of B|C: '))
                break
            except:
                print('Invalid input detected -- try again!')
        
        while True:
            try:
                BgivenNotC = float(input('Enter probability of B|C\': '))
                break
            except:
                print('Invalid input detected -- try again!')
                
        CgivenB = PerformBaysianCalculation(C, BgivenC, BgivenNotC)
        
        PrintBayesianProbability(CgivenB)        
        
        try:
            again = input('Would you like to do another calculation? (y/n) ')
        except:
            break
        
        if again is not 'y':
            break
        
def Main():
    print('\nIn this program we will simulate coin flips and calculate a Baysian value')
    input('Press enter to proceed. ')
    CoinFlipSimulator()
    CalculateBayesProbability()
        
Main()