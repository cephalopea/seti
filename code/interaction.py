# This module covers all interactions between civilizations,
# including war, and communication
import evolution

def Attack(attacker, civDistance): #construct an attack
    attackTime = Math.floor(civDistance/attacker.arms) #when will this attack land?
    attackDamage = attacker.dev #how much damage will this attack deal?
    return {"time": attackTime, "damage": attackDamage} #return dict containing those two values
    
def Communicate():
    return True