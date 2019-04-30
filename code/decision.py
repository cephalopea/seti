# This module covers the decision-making functions and payoff matrices
# of civilizations when they are interacting.
import random as rd
import civilization

strategies = ["attack", "communicate"]

# this payoff matrix should be updated every round, but civs don't recieve payoffs til game concludes
#
#           A                   C
#   _______________________________________
# A | 1-2 \ 2-1 | 0 \ 2-1                 |
#   |_____________________________________|
# C | 1-2 \ 0   | 1+ (1+2/5) \ 2+ (1+2/5) |
#   |_____________________________________|

def EstimateMatrix(civ1, civ2):
    aA = [(civ1.dev - civ2.dev), (civ2.dev - civ1.dev)] #civ 1 attacks, civ 2 attacks
    aC = [0, (civ2.dev - civ1.dev)] #civ 1 attacks, civ 2 communicates
    cA = [(civ1.dev - civ2.dev), 0] #civ 1 communicates, civ 2 attacks
    cC [(civ1.dev + (civ1.dev + civ2.dev)/5), (civ2.dev + (civ1.dev + civ2.dev)/5)] #civ 1 communicates, civ 2 communicates
    return [aA, aC, cA, cC] #return array representing predicted payoffs

def ChooseActions(civ1, civ2):
    estMatrix = EstimateMatrix(civ1, civ2)
    civ1Payoff = [(estMatrix[0][0] + estMatrix[1][0])/2, (estMatrix[2][0] + estMatrix[3][0])/2] #assuming opponent is playing "randomly", get avg utils
    civ2Payoff = [(estMatrix[0][1] + estMatrix[2][1])/2, (estMatrix[1][1] + estMatrix[3][1])/2] #payoff structure: [attack, communicate]
    civ1Action = None
    civ2Action = None
    if (civ1Payoff[0] > civ1Payoff[1]):
        civ1Action = "attack"
    else if (civ1Payoff[0] == civ1Payoff[1]):
        civ1Action = strategies[rd.randint(0,1)]
    else:
        civ1Action = "communicate"
    if (civ2Payoff[0] > civ2Payoff[1]):
        civ2Action = "attack"
    else if (civ2Payoff[0] == civ2Payoff[1]):
        civ2Action = strategies[rd.randint(0,1)]
    else:
        civ2Action = "communicate"
    return [civ1Action, civ2Action]
        