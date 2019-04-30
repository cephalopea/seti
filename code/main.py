import numpy as np
import random as rd
import civilization

civ1Dev = None
civ1Arms = None
civ1Agg = None
civ1Comm = None

civ2Dev = None
civ2Arms = None
civ2Agg = None
civ2Comm = None

civDistance = 1 #in lightyears??? dunno yet, we'll get there

def GetCustomCivSettings():
    #get user input for civ 1 and civ 2 traits and assign it to vars above, plus distance?
    
def Communicate():
    #one round between the civs

def Main(getUserInput):
    if (getUserInput):
        GetCustomCivSettings()
    civ1 = civilization.civ(civ1Dev, civ1Arms, civ1Agg, civ1Comm)
    civ2 = civilization.civ(civ2Dev, civ2Arms, civ2Agg, civ2Comm)
    #do we need something for distance? how do we know how many times civs can communicate?
