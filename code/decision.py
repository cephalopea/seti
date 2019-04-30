# This module covers the decision-making functions and payoff matrices
# of civilizations when they are interacting.
import random as rd
import civilization

# this payoff matrix is updated every round, but this is the general structure
#
#                     civ2
#           A                      C
#         _________________________________________________________________
#      A | civ1-civ2 \ civ2-civ1 | 0 \ civ2-civ1                           |
# civ1   |_______________________|_________________________________________|
#      C | civ1-civ2 \ 0         | civ1+(civ1+civ2/5) \ civ2+(civ1+civ2/5) |
#        |_______________________|_________________________________________|

strategies = ["attack", "communicate"]

def EstimateMatrix(civ1, civ2): #create matrix for the current round of the game
    aA = [(civ1.dev - civ2.dev), (civ2.dev - civ1.dev)] #civ 1 attacks, civ 2 attacks
    aC = [0, (civ2.dev - civ1.dev)] #civ 1 attacks, civ 2 communicates
    cA = [(civ1.dev - civ2.dev), 0] #civ 1 communicates, civ 2 attacks
    cC = [(civ1.dev + (civ1.dev + civ2.dev)/5), (civ2.dev + (civ1.dev + civ2.dev)/5)] #civ 1 communicates, civ 2 communicates
    return [aA, aC, cA, cC] #return array representing predicted payoffs

def ChooseActions(civ1, civ2): #decide what each civ should do
    estMatrix = EstimateMatrix(civ1, civ2)
    civ1Payoff = [(estMatrix[0][0] + estMatrix[1][0])*civ1.agg, (estMatrix[2][0] + estMatrix[3][0])*(1-civ1.agg)] #assuming opponent is playing "randomly", get avg utils
    civ2Payoff = [(estMatrix[0][1] + estMatrix[2][1])*civ2.agg, (estMatrix[1][1] + estMatrix[3][1])*(1-civ2.agg)] #payoff structure: [attack, communicate]
    civ1Action = None #instantiate civ 1's action as None
    civ2Action = None #instantiate civ 2's action as None
    if (civ1Payoff[0] > civ1Payoff[1]): #if civ 1 has a better payoff for attacking
        civ1Action = "attack" #attack
    elif (civ1Payoff[0] == civ1Payoff[1]): #if civ 1's payoffs are equal
        civ1Action = strategies[rd.randint(0,1)] #do something random
    else: #if civ 1 has a better payoff for communicating
        civ1Action = "communicate" #communicate
    if (civ2Payoff[0] > civ2Payoff[1]): #if civ 2 has a better payoff for attacking
        civ2Action = "attack" #attack
    elif (civ2Payoff[0] == civ2Payoff[1]): #if civ 2's payoffs are equal
        civ2Action = strategies[rd.randint(0,1)] #do something random
    else: #if civ 2 has a better payoff for communicating
        civ2Action = "communicate" #communicate
    return [civ1Action, civ2Action] #return their decisions
        