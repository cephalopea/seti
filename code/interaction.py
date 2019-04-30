# This module covers all interactions between civilizations,
# including war, and communication
import evolution

def Attack(attacker, civDistance): #construct an attack
    attackTime = Math.floor(civDistance/attacker.arms) #in how many rounds will this attack land?
    attackDamage = (0 - attacker.dev) #how much damage will this attack deal? this should be negative
    return {"time": attackTime, "impact": attackDamage} #return dict containing those two values
    
def Communicate(): #not sure what we want to do with communication
    communicateTime = civDistance #communication takes 1 round
    communicatePayoff = 0 #this is just 0 for now
    return {"time": communicateTime, "impact": communicatePayoff} #structured the same as attack