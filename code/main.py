import threading
import numpy as np
import random as rd
import pandas as pd
import math
import civilization
import evolution
import decision
import interaction

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
    
    return {"civ1": {"dev": civ1Dev, "arms": civ1Arms, "agg": civ1Agg, "comm": civ1Comm}, "civ2": {"dev": civ2Dev, "arms": civ2Arms, "agg": civ2Agg, "comm": civ2Comm}, "dist": civDistance}

def GetStandardCivSettings():
    civ1Dev = 1
    civ1Arms = 0.2
    civ1Agg = 1
    civ1Comm = 1

    civ2Dev = 1
    civ2Arms = 0.2
    civ2Agg = 1
    civ2Comm = 1
    
    civDistance = 5
    
    return {"civ1": {"dev": civ1Dev, "arms": civ1Arms, "agg": civ1Agg, "comm": civ1Comm}, "civ2": {"dev": civ2Dev, "arms": civ2Arms, "agg": civ2Agg, "comm": civ2Comm}, "dist": civDistance}

def GetRandomCivSettings():
    civ1Dev = round(rd.uniform(0,2), 2) #random number between 0 and 2 with 2 decimal places
    civ1Arms = round(1 - math.sqrt(1 - rd.uniform(0,1)), 5) #random number between 0 and 1, weighted towards 0
    civ1Agg = round(rd.uniform(0,1), 2) #random number between 0 and 1 with 2 decimal places
    civ1Comm = round(rd.uniform(0,2), 2) #random number between 0 and 2 with 2 decimal places
    
    civ2Dev = round(rd.uniform(0,2), 2) #random number between 0 and 2 with 2 decimal places
    civ2Arms = round(1 - math.sqrt(1 - rd.uniform(0,1)), 5) #random number between 0 and 1, weighted towards 0
    civ2Agg = round(rd.uniform(0,1), 2) #random number between 0 and 1 with 2 decimal places
    civ2Comm = round(rd.uniform(0,2), 2) #random number between 0 and 2 with 2 decimal places
    
    civDistance = math.ceil(rd.randint(1,10))
    
    return {"civ1": {"dev": civ1Dev, "arms": civ1Arms, "agg": civ1Agg, "comm": civ1Comm}, "civ2": {"dev": civ2Dev, "arms": civ2Arms, "agg": civ2Agg, "comm": civ2Comm}, "dist": civDistance}

def Main(getUserInput):
    civInputs = None
    if (getUserInput): #if we want user input
        civInputs = GetCustomCivSettings() #get user input
    else:
        civInputs = GetRandomCivSettings()
    civ1 = civilization.civ(civInputs["civ1"]["dev"], civInputs["civ1"]["arms"], civInputs["civ1"]["agg"], civInputs["civ1"]["comm"]) #init civ 1 using values (default or user input)
    civ2 = civilization.civ(civInputs["civ2"]["dev"], civInputs["civ2"]["arms"], civInputs["civ2"]["agg"], civInputs["civ2"]["comm"]) #init civ 2 using values (default or user input)
    
    civDistance = civInputs["dist"]
    
    print("Civ 1 | Development:", civ1.dev, "| Arms Speed:", civ1.arms, "| Aggressiveness:", civ1.agg, "| Communication:", civ1.comm)
    print("Civ 2 | Development:", civ2.dev, "| Arms Speed:", civ2.arms, "| Aggressiveness:", civ2.agg, "| Communication:", civ2.comm)
    print("Civ Distance:", civDistance)
    
    currentRound = 0
    consecutiveComm = 0
    attackRounds = 0 #instantiate number of rounds
    if (civ1.arms < civ2.arms): #if civ 1 is slower than civ 2
        attackRounds = math.ceil(civDistance/civ1.arms) #rounds for the slower civ to nuke the faster civ
    else: #otherwise civ 2 is slower
        attackRounds = math.ceil(civDistance/civ2.arms) #same as above
    #this while condition is really long:
    #checks that neither civ is dead, we haven't timed out, and we haven't established trust
    while (civ1.dev > 0) and (civ2.dev > 0) and (currentRound < 10*attackRounds) and (consecutiveComm < attackRounds):
        #check to see if any pending actions are realized this turn
        civ1Actionable = filter(interaction.CheckPending, civ1.pending) #find the items that are happening this turn
        for action in civ1Actionable: #for each of those items
            civ1.dev += action["impact"] #add their impact (pos or neg) to development
        civ2Actionable = filter(interaction.CheckPending, civ2.pending) #do same steps for civ 2
        for action in civ2Actionable:
            civ2.dev += action["impact"]
            
        #once development scores are altered, decide what to do next
        est = decision.ChooseActions(civ1, civ2) #get the decisions of each civ
        
        #keep track of consecutive communication count
        if ((est[0] == "communicate") and (est[1] == "communicate")): #if both communicated
            consecutiveComm += 1 #increase their comm count
        else: #if one attacked
            consecutiveComm = 0 #zero out comm count
            
        #handle actions for this turn
        if (est[0] == "attack"): #civ 1 attacked
            civ2.pending.append(interaction.Attack(civ1, civDistance)) #add an attack to civ 2's pending
        else: #civ 1 communicated
            civ2.pending.append(interaction.Communicate(civ1, civDistance)) #add a communication to civ 2's pending
        if(est[1] == "attack"): #civ 2 attacked
            civ1.pending.append(interaction.Attack(civ2, civDistance)) #add an attack to civ 1's pending
        else:
            civ1.pending.append(interaction.Communicate(civ2, civDistance)) #add a communication to civ 1's pending
            
        currentRound += 1 #increment current round for timeout
            
    #the game has concluded, figure out why
    print("Rounds Elapsed:", currentRound)
    if (civ1.dev <= 0) and (civ2.dev > 0): #civ1 is dead and civ2 is alive
        print("Civ 2 Annihilates Civ  1")
    elif (civ2.dev <=0) and (civ1.dev > 0): #civ2 is dead and civ1 is alive
        print("Civ 1 Annihilates Civ 2")
    elif (civ2.dev <=0) and (civ1.dev <= 0): #everyone's dead
        print("Everyone Has Died")
    elif (currentRound >= 10*attackRounds): #we've timed out
        print("Stalemate")
    elif (consecutiveComm >= attackRounds): #we've established trust
        print("Trust Established")
    else:
        print("Error Encountered")
    return True

def runTrials(param):
    print("runTrials of "+param)
    data=[["civ1 dev"],["civ1 arms"],["civ1 agg"],["civ1 com"],["civ2 dev"],["civ2 arms"],["civ2 agg"],["civ2 com"],["dist"],["rounds"],["outcome"]]
    for i in range(20):
        if(i%2==0):
            print(param, i)
        for j in range(20):
            civInputs = GetStandardCivSettings()
            civ1 = civilization.civ(civInputs["civ1"]["dev"], civInputs["civ1"]["arms"], civInputs["civ1"]["agg"], civInputs["civ1"]["comm"]) #init civ 1 using values (default or user input)
            civ2 = civilization.civ(civInputs["civ2"]["dev"], civInputs["civ2"]["arms"], civInputs["civ2"]["agg"], civInputs["civ2"]["comm"]) #init civ 2 using values (default or user input)
            
            civDistance = civInputs["dist"]

            if(param=="dist"):
                civDistance=i//2
            elif(param=="dev"):
                civ1.dev=i/10
                civ2.dev=j/10
            elif(param=="arms"):
                civ1.arms=1-math.sqrt(i/20)
                civ2.arms=1-math.sqrt(j/20)
            elif(param=="agg"):
                civ1.agg=i/20
                civ2.agg=j/20
            elif(param=="comm"):
                civ1.comm=i/10
                civ2.comm=j/10
            elif(param=="randomize"):
                civInputs=GetRandomCivSettings()
                civ1 = civilization.civ(civInputs["civ1"]["dev"], civInputs["civ1"]["arms"], civInputs["civ1"]["agg"], civInputs["civ1"]["comm"]) #init civ 1 using values (default or user input)
                civ2 = civilization.civ(civInputs["civ2"]["dev"], civInputs["civ2"]["arms"], civInputs["civ2"]["agg"], civInputs["civ2"]["comm"]) #init civ 2 using values (default or user input)
            
                civDistance = civInputs["dist"]
            else:
                print("invalid parameter")
                return

            data[0].append(civ1.dev)
            data[1].append(civ1.arms)
            data[2].append(civ1.agg)
            data[3].append(civ1.comm)

            data[4].append(civ2.dev)
            data[5].append(civ2.arms)
            data[6].append(civ2.agg)
            data[7].append(civ2.comm)

            data[8].append(civDistance)
            
            currentRound = 0
            consecutiveComm = 0
            attackRounds = 0 #instantiate number of rounds
            if (civ1.arms < civ2.arms): #if civ 1 is slower than civ 2
                attackRounds = math.ceil(civDistance/civ1.arms) #rounds for the slower civ to nuke the faster civ
            else: #otherwise civ 2 is slower
                attackRounds = math.ceil(civDistance/civ2.arms) #same as above
            #this while condition is really long:
            #checks that neither civ is dead, we haven't timed out, and we haven't established trust
            while (civ1.dev > 0) and (civ2.dev > 0) and (currentRound < 10*attackRounds) and (consecutiveComm < attackRounds):
                #check to see if any pending actions are realized this turn
                civ1Actionable = filter(interaction.CheckPending, civ1.pending) #find the items that are happening this turn
                for action in civ1Actionable: #for each of those items
                    civ1.dev += action["impact"] #add their impact (pos or neg) to development
                civ2Actionable = filter(interaction.CheckPending, civ2.pending) #do same steps for civ 2
                for action in civ2Actionable:
                    civ2.dev += action["impact"]
                    
                #once development scores are altered, decide what to do next
                est = decision.ChooseActions(civ1, civ2) #get the decisions of each civ
                
                #keep track of consecutive communication count
                if ((est[0] == "communicate") and (est[1] == "communicate")): #if both communicated
                    consecutiveComm += 1 #increase their comm count
                else: #if one attacked
                    consecutiveComm = 0 #zero out comm count
                    
                #handle actions for this turn
                if (est[0] == "attack"): #civ 1 attacked
                    civ2.pending.append(interaction.Attack(civ1, civDistance)) #add an attack to civ 2's pending
                else: #civ 1 communicated
                    civ2.pending.append(interaction.Communicate(civ1, civDistance)) #add a communication to civ 2's pending
                if(est[1] == "attack"): #civ 2 attacked
                    civ1.pending.append(interaction.Attack(civ2, civDistance)) #add an attack to civ 1's pending
                else:
                    civ1.pending.append(interaction.Communicate(civ2, civDistance)) #add a communication to civ 1's pending
                    
                currentRound += 1 #increment current round for timeout
                    
            #the game has concluded, figure out why
            data[9].append(currentRound)
            if (civ1.dev <= 0) and (civ2.dev > 0): #civ1 is dead and civ2 is alive
                data[10].append("Civ 2 Annihilates Civ 1")
            elif (civ2.dev <=0) and (civ1.dev > 0): #civ2 is dead and civ1 is alive
                data[10].append("Civ 1 Annihilates Civ 2")
            elif (civ2.dev <=0) and (civ1.dev <= 0): #everyone's dead
                data[10].append("Everyone Has Died")
            elif (currentRound >= 10*attackRounds): #we've timed out
                data[10].append("Stalemate")
            elif (consecutiveComm >= attackRounds): #we've established trust
                data[10].append("Trust Established")
            else:
                data[10].append("Error Encountered")

            if(param=="dist"):
                break

    np_array=np.transpose(np.asarray(data))
    pd.DataFrame(np_array).to_csv("./"+param+"_data.csv")


def getData():
    t_dist=threading.Thread(target=runTrials, args=("dist",))
    t_dev=threading.Thread(target=runTrials, args=("dev",))
    t_arms=threading.Thread(target=runTrials, args=("arms",))
    t_agg=threading.Thread(target=runTrials, args=("agg",))
    t_comm=threading.Thread(target=runTrials, args=("comm",))

    t_dist.start()
    t_dev.start()
    t_arms.start()
    t_agg.start()
    t_comm.start()

    t_dist.join()
    t_dev.join()
    t_arms.join()
    t_agg.join()
    t_comm.join()

 #   runTrials("randomize")
 
            
        
Main(False)
