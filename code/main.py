import numpy as np
import random as rd
import civilization
import evolution
import decision
import interaction

civ1Dev = None
civ1Arms = None
civ1Agg = None
civ1Comm = None

civ2Dev = None
civ2Arms = None
civ2Agg = None
civ2Comm = None

civDistance = 1 #default val in lightyears

def GetCustomCivSettings():
    #get user input for civ 1 and civ 2 traits and assign it to vars above, plus distance?
    print("Civ 1 Development: ")
    civ1Dev = input()
    print("Civ 1 Arms Deployment Speed: ")
    civ1Arms = input()
    print("Civ 1 Aggression: ")
    civ1Agg = input()
    print("Civ 1 Communication: ")
    civ1Comm = input()
    
    print("Civ 2 Development: ")
    civ2Dev = input()
    print("Civ 2 Arms Deployment Speed: ")
    civ2Arms = input()
    print("Civ 2 Aggression: ")
    civ2Agg = input()
    print("Civ 2 Communication: ")
    civ2Comm = input()
    
    print("Distance Between Civilizations (in lightyears): ")
    civDistance = input()
    
    return True  

def Main(getUserInput):
    if (getUserInput): #if we want user input
        GetCustomCivSettings() #get user input
    civ1 = civilization.civ(civ1Dev, civ1Arms, civ1Agg, civ1Comm) #init civ 1 using values (default or user input)
    civ2 = civilization.civ(civ2Dev, civ2Arms, civ2Agg, civ2Comm) #init civ 2 using values (default or user input)
    currentRound = 0
    consecutiveComm = 0
    attackRounds = 0 #instantiate number of rounds
    if (civ1.arms < civ2.arms): #if civ 1 is slower than civ 2
        attackRounds = Math.ceil(civDistance/civ1.arms) #rounds for the slower civ to nuke the faster civ
    else: #otherwise civ 2 is slower
        attackRounds = Math.ceil(civDistance/civ2.arms) #same as above
    while ((civ1.dev > 0) && (civ2.dev > 0) && (currentRound < 10*attackRounds)): #nobody's dead and we haven't timed out
        est = decision.ChooseActions(civ1, civ2) #get the decisions of each civ
        if ((est[0] == "communicate") && (est[1] == "communicate")): #if both communicated
            consecutiveComm += 1 #increase their comm count
        else: #if one attacked
            consecutiveComm = 0 #zero out comm count
        if (consecutiveComm >= attackRounds): #if we've communicated enough rounds to know neither has attacked since we started communicating
            break #success! trust established!
        
        
    
    
