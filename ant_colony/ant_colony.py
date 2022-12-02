import time
import random
import math

# test file = ../test_files/large_scale/knapPI_1_100_1000_1

#/!\/!\ can be opti = you can try to modify it while you have the same structur
#/!\/!\ do not change = destroy algo if you change it !
#/!\/!\

# params change result
ALPHA = 2
RHO = 0.98
BETA = 5

# params don't change result (don't change them)
MINPHERO = 0.01
MAXPHERO = 6


def defCandi(candidates, list_objects) : # can be opti ?
    for i in range(len(list_objects)):
        candidates.update({i : 1})

def defPhero(phero, list_objects) : # can be opti ?
    for j in range(len(list_objects)):
        tmp = [0]
        for i in range(len(list_objects)):
            tmp.append(0 if j == i else MAXPHERO)
        phero.update({j : tmp})
    tmp[-1]=MAXPHERO
    phero.update({len(list_objects) : tmp})
    

def sumPheroValue(phero,list_objects,candidates,current) : # do not change !!!
    # Sum of pheromones depending of the curent item
    sum=0
    for i in range(len(list_objects)) :
        if candidates[i] == 1 :
            sum += math.pow(phero[current][i],ALPHA)*math.pow((list_objects[i][0]/list_objects[i][1]),BETA)
    if sum == 0 :
        sum = 0.01 
    return sum

def updatePhero(phero): # do not change !!!
    # Evaporation of pheromones 
    # The min quantity of pheromones is MINPHERO
    for i in phero.items() :
        
        if phero[i[0]][0]*RHO < MINPHERO :
            phero[i[0]][0] = MINPHERO
        else :
            phero[i[0]][0] = phero[i[0]][0]*RHO
            
        for j in phero.items():
            if i[0] == j[0] :
                phero[i[0]][j[0]] = 0
            elif phero[i[0]][j[0]]*RHO < MINPHERO :
                phero[i[0]][j[0]] = MINPHERO
            else :
                phero[i[0]][j[0]] = phero[i[0]][j[0]]*RHO
                
def setPhero(phero,bestSolution,currentSolution): # do not change !!!
    # The quantity of pheromones set on the solution by ants depending on value and weigth of the solution and the best solution
    p = 1/(1+bestSolution['value']-currentSolution['value'])
    prec = 0
    for i in currentSolution["number"] :
        if phero[i][prec]+p > MAXPHERO :
            phero[i][prec] = MAXPHERO
            phero[prec][i] = MAXPHERO
        else :
            phero[i][prec] = phero[i][prec]+p
            phero[prec][i] = phero[prec][i]+p
        prec = i

def setProb(probabilities, phero ,list_objects,candidates,current): # do not change !!!
    # Calculate the probabilities for each items depending of the current item
    p = sumPheroValue(phero,list_objects,candidates,current)
    maxProb = 0
    for i in candidates.items():
        # Calculate only for items candidates
        if i[1] == 1 :
            minProb = maxProb
            maxProb += (math.pow(phero[current][i[0]],ALPHA)*math.pow((list_objects[i[0]][0]/list_objects[i[0]][1]),BETA))/p
            probabilities.update({i[0] : [minProb, maxProb]})

def ant(list_objects,nbAnts,n,wmax):
    # For the time of execution
    start_process = time.time()

    # Initialize the pheromones table ---------------------
    phero = {}
    defPhero(phero, list_objects)

    # Create the probabilities table ----------------------
    probabilities = {}

    # Create the save of the best solution ----------------
    bestSolution ={'number' :[], 'objects' : [],'value' : -1 , 'weight': -1}
    
    # Ant loop --------------------------------------------
    for ant in range(nbAnts) :
        # Create the current solution
        currentSolution = {'number' :[], 'objects' : [], 'value' : 0 , 'weight': 0}
        
        # Create candidates list
        candidates = {}
        defCandi(candidates, list_objects)

        # Number of items check
        cantGo = 0

        # Set the current item to 0 (empty bag)
        current = 0

        #First item
        x = random.random()

        # Set probabilities for 0 (empty bag)
        setProb(probabilities,phero,list_objects,candidates,current)
            
        # Get the first item 
        for j in probabilities.items():
            if x >= j[1][0] and x < j[1][1] and (currentSolution["weight"]+list_objects[j[0]][1]) <= wmax:
                # Remove j of cantidates
                candidates.update({j[0] : 0})
                # Remove the pobability of j
                probabilities.update({j[0] : [-1, -1]}) # do not change !!!
                # Save j in the current solution
                currentSolution["number"].append(j[0])
                currentSolution["objects"].append(list_objects[j[0]])
                currentSolution["value"] += list_objects[j[0]][0]
                currentSolution["weight"] += list_objects[j[0]][1]
                # Put j in the current item
                current = j[0]
                # Incrase item check
                cantGo += 1
                # If we found the item we don't need to check the others
                break
        
        # While we didin't check all items
        while cantGo <= n :
            # Next item
            x = random.random()
            # Update probabilities for the current item
            setProb(probabilities,phero,list_objects,candidates,current)
            for j in probabilities.items():
                # Get the next item
                if x >= j[1][0] and x < j[1][1] and (currentSolution["weight"]+list_objects[j[0]][1]) <= wmax:
                    # Remove j of candidates
                    candidates.update({j[0] : 0})
                    # Remove the probability of j
                    probabilities.update({j[0] : [-1, -1]}) # do not change !!!
                    # Save j in the current item
                    currentSolution["number"].append(j[0])
                    currentSolution["objects"].append(list_objects[j[0]])
                    currentSolution["value"] += list_objects[j[0]][0]
                    currentSolution["weight"] += list_objects[j[0]][1]
                    # Put j in the current item
                    current = j[0]
                    # Incrase item check
                    cantGo += 1
                    # If xe found the item we don't need to check the others
                    break
                # If the items is too heavy
                elif (currentSolution["weight"]+list_objects[j[0]][1]) > wmax :
                    # Remove j of candidates
                    candidates.update({j[0] : 0})
                    # Remove the probability of j
                    probabilities.update({j[0] : [-1, -1]}) # do not change !!!
                    # Incrase item check
                    cantGo += 1
            
        # Check if the current solution is better than the best solution
        if currentSolution["value"] > bestSolution["value"] :
            # Save the current solution in best solution
            bestSolution = currentSolution
            
        # Evaporation of pheromones
        updatePhero(phero)
        # Set pheromones on the current solution
        setPhero(phero,bestSolution,currentSolution)
        
    # For time of execution
    end_process = time.time()

    # Just to show the best solution 
    #print(f"{bestSolution['objects']}\nweith : {bestSolution['weight']}/{wmax}\ntime : {end_process-start_process}\n")
    return (end_process- start_process), bestSolution["objects"], bestSolution["value"]

def sumPheroValue_multid(phero,list_objects,ndim,candidates,current) : # do not change !!!
    # Sum of pheromones depending of the curent item
    sum=0
    for i in range(len(list_objects)) :
        w = 0
        for tmp in range(1,ndim):
            w += list_objects[i][tmp]
        if candidates[i] == 1 :
            sum += math.pow(phero[current][i],ALPHA)*math.pow((list_objects[i][0]/(w/15)),BETA)
    return sum

def setProb_multid(probabilities, phero, ndim ,list_objects,candidates,current): # do not change !!!
    # Calculate the probabilities for each items depending of the current item
    p = sumPheroValue_multid(phero, list_objects, ndim, candidates, current)
    maxProb = 0
    for i in candidates.items():
        # Calculate only for items candidates
        if i[1] == 1 :
            w = 0
            for tmp in range(ndim):
                w += list_objects[i[0]][tmp]

            minProb = maxProb
            maxProb += (math.pow(phero[current][i[0]],ALPHA)*math.pow((list_objects[i[0]][0]/w),BETA))/p
            probabilities.update({i[0] : [minProb, maxProb]})

def ant_multid(list_objects,ndim,nbAnts,n,wmax):
    # For the time of execution
    start_process = time.time()

    # Initialize the pheromones table ---------------------
    phero = {}
    defPhero(phero, list_objects)

    # Create the probabilities table ----------------------
    probabilities = {}

    # Create the save of the best solution ----------------
    bestSolution ={'number' :[], 'objects' : [],'value' : -1 , 'weight': [-1 for i in range(ndim+1)]}
    
    # Ant loop --------------------------------------------
    for ant in range(nbAnts) :
        # Create the current solution
        currentSolution = {'number' :[], 'objects' : [], 'value' : 0 , 'weight': [0 for i in range(ndim+1)]}
        
        # Create candidates list
        candidates = {}
        defCandi(candidates, list_objects)

        # Number of items check
        cantGo = 0

        # Set the current item to 0 (empty bag)
        current = 0

        #First item
        x = random.random()

        # Set probabilities for 0 (empty bag)
        setProb_multid(probabilities, phero, ndim, list_objects, candidates, current)
        
        # Check all dimensions 
        ok = True

        # Get the first item 
        for j in probabilities.items():
            # Check the probabilitie 
            if x >= j[1][0] and x < j[1][1] :
                # Check if all dimension are ok
                for tmp in range(1,ndim) :
                    if (currentSolution["weight"][tmp]+list_objects[j[0]][tmp]) > wmax[tmp-1]:
                        ok = False
                        break
                
                if ok :
                    # Remove j of cantidates
                    candidates.update({j[0] : 0})
                    # Remove the pobability of j
                    probabilities.update({j[0] : [-1, -1]}) # do not change !!!
                    # Save j in the current solution
                    currentSolution["number"].append(j[0])
                    currentSolution["objects"].append(list_objects[j[0]])
                    currentSolution["value"] += list_objects[j[0]][0]
                    # Add all weights
                    for tmp in range(ndim) :
                        currentSolution["weight"][tmp] += list_objects[j[0]][tmp]
                    # Put j in the current item
                    current = j[0]
                    # Incrase item check
                    cantGo += 1
                    # If we found the item we don't need to check the others
                
                break
        
        # While we didin't check all items
        while cantGo <= n :
            # Next item
            x = random.random()
            # Check for weights
            ok = True
            # Update probabilities for the current item
            setProb_multid(probabilities, phero, ndim, list_objects, candidates, current)
            for j in probabilities.items():
                # Get the next item
                if x >= j[1][0] and x < j[1][1] : 
                    for tmp in range(1,ndim):
                        if (currentSolution["weight"][tmp]+list_objects[j[0]][tmp]) > wmax[tmp]:
                            # If the items is too heavy
                            ok = False
                            # Remove j of candidates
                            candidates.update({j[0] : 0})
                            # Remove the probability of j
                            probabilities.update({j[0] : [-1, -1]}) # do not change !!!
                            # Incrase item check
                            cantGo += 1
                            break
                    if ok :
                        # Remove j of candidates
                        candidates.update({j[0] : 0})
                        # Remove the probability of j
                        probabilities.update({j[0] : [-1, -1]}) # do not change !!!
                        # Save j in the current item
                        currentSolution["number"].append(j[0])
                        currentSolution["objects"].append(list_objects[j[0]])
                        currentSolution["value"] += list_objects[j[0]][0]
                        # Add all weights
                        for tmp in range(ndim) :
                            currentSolution["weight"][tmp] += list_objects[j[0]][tmp]
                        # Put j in the current item
                        current = j[0]
                        # Incrase item check
                        cantGo += 1
                        # If xe found the item we don't need to check the others
                        break
                
            
        # Check if the current solution is better than the best solution
        if currentSolution["value"] > bestSolution["value"] :
            # Save the current solution in best solution
            bestSolution = currentSolution
            
        # Evaporation of pheromones
        updatePhero(phero)
        # Set pheromones on the current solution
        setPhero(phero,bestSolution,currentSolution)
        
    # For time of execution
    end_process = time.time()

    # Just to show the best solution 
    print(f"{bestSolution['objects']}\nvalue : {bestSolution['value']}\ntime : {end_process-start_process}\n")
    
    #return (end_process- start_process), bestSolution["objects"], bestSolution["value"]

if __name__=="__main__":
    try :
        file = input("file name : ")

        with open(file, "r") as f:
            data = f.read()
            line = data.split("\n")
        
        # First with the number of object and the capacity of the knapsack
        nbo, ksc = line[0].split()
        
        n = int(nbo) # number of object
        wmax = int(ksc) # Maximum weight

        # Proceeding every object and giving the time needed to process the file
        list_objects = [] 
        for i in range(1, n+1):
            oval, owei = line[i].split()
            list_objects.append((int(oval), int(owei)))
        else :
            print("Finished loading the objects !\n")

        nbAnts = int(input("How many ants : "))

        ant(list_objects,nbAnts,n,wmax)
        
    except KeyboardInterrupt:
        """ To stop the program ! """
        print("\nBye !")
        quit()
    except FileNotFoundError:
        """ If file not exist ! """
        print("The file doesn't exist !\nBye !\n")
        quit()
