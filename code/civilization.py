import numpy as np
import random as rd

##### Global Constants #####

# Development
#The level of the civilization's development,
#described by its placement on the Kardashev scale.
# A range between 0.0 and 2.0 for the purposes of this project.
Development = 0.7

# Communication
#Communication constant. The ratio between the Development of a civilization and
#its ability to send and recieve signals from other civilizations.
Communication = 1.0

# Speed
#The default ratio between the speed of light and the speed of a civilization's
#weapons of mass destruction.
#Number is the top speed of Juno, divided by the speed of light
Speed = 0.00025

# Aggression
#A score representing a civilization's tendencies towards aggression.
#A score of 0.0 represents a civilization that never acts aggressively.
#A score of 1.0 represents a civilization that always acts aggressively.
Aggression = 0.5


##### Civilization Class #####

class civ:
    # Development
    #The level of the civilization's development,
    #described by its placement on the Kardashev scale.
    # A range between 0.0 and 2.0 for the purposes of this project.
    dev = Development

    # Arms Deployment Speed
    #The speed of a weapon launched by this civilization
    #In terms of a fraction of the speed of light
    arms = Speed

    # Communication Score
    #A score representing a civilization's ability to communicate with other civilizations.
    comm = Communication * dev

    # Aggression
    #A score representing a civilization's tendencies towards aggression.
    #A score of 0.0 represents a civilization that never acts aggressively.
    #A score of 1.0 represents a civilization that always acts aggressively.
    agg = Aggression
    
    # Pending
    #Contains all the pending actions happening to this user
    pending = []

    def __init__(self, Devel = None, Arms_Deployment_Speed = None, Aggressiveness = None, Communication_Score = None):
        if Devel is None:
            self.dev = Development
        else:       
            self.dev = Devel
        if Arms_Deployment_Speed is None:
            self.arms = Speed
        else:    
            self.arms = Arms_Deployment_Speed
        if Aggressiveness is None:
            self.agg = Aggression
        else:    
            self.agg = Aggressiveness
        if Communication_Score is None:
            self.comm = Communication * self.dev
        else:    
            self.comm = Communication_Score
        pending = []

# Earth has a development value of 0.7.
Earth = civ()
print(Earth.comm)