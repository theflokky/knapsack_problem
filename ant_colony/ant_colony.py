import time
import random
import math

# test file = ../test_files/large_scale/knapPI_1_200_1000_1

#/!\/!\ can be opti = you can try to modify it while you have the same structur
#/!\/!\ do not change = destroy algo if you change it !
#/!\/!\

# params change result
ALPHA = 1
RHO = 0.98
BETA = 5

# params don't change result (don't change them)
MINPHERO = 0.01
MAXPHERO = 6


def defCandi(candidates) : # can be opti ?
    for i in objects.items():
        candidates.update({i[0] : 1})

def defPhero(phero) : # can be opti ?
    for j in objects.items():
        tmp = [0]
        for i in objects.items():
            tmp.append(0 if j[0] == i[0] else MAXPHERO)
        phero.update({j[0] : tmp})
    tmp[-1]=MAXPHERO
    phero.update({0 : tmp})
    

def sumPheroValue(phero,objects,candidates,current) : # do not change !!!
    # Sum of pheromones depending of the curent item
    sum=0
    for i in objects.items() :
        if candidates[i[0]] == 1 :
            sum += math.pow(phero[current][i[0]],ALPHA)*math.pow((objects[i[0]][0]/objects[i[0]][1]),BETA) 
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

def setProb(probabilities, phero ,objects,candidates,current): # do not change !!!
    # Calculate the probabilities for each items depending of the current item
    p = sumPheroValue(phero,objects,candidates,current)
    maxProb = 0
    for i in candidates.items():
        # Calculate only for items candidates
        if i[1] == 1 :
            minProb = maxProb
            maxProb += (math.pow(phero[current][i[0]],ALPHA)*math.pow((objects[i[0]][0]/objects[i[0]][1]),BETA))/p
            probabilities.update({i[0] : [minProb, maxProb]})

def ant(objects,nbAnts):
    # For the time of execution
    start_process = time.time()

    # Initialize the pheromones table ---------------------
    phero = {}
    defPhero(phero)

    # Create the probabilities table ----------------------
    probabilities = {}

    # Create the save of the best solution ----------------
    bestSolution ={'number' :[], 'value' : -1 , 'weight': -1}
    
    # Ant loop --------------------------------------------
    for ant in range(nbAnts) :
        # Create the current solution
        currentSolution = {'number' :[], 'value' : 0 , 'weight': 0}
        
        # Create candidates list
        candidates = {}
        defCandi(candidates)

        # Number of items check
        cantGo = 0

        # Set the current item to 0 (empty bag)
        current = 0

        #First item
        x = random.random()

        # Set probabilities for 0 (empty bag)
        setProb(probabilities,phero,objects,candidates,current)
            
        # Get the first item 
        for j in probabilities.items():
            if x >= j[1][0] and x < j[1][1] and (currentSolution["weight"]+objects[j[0]][1]) <= wmax:
                # Remove j of cantidates
                candidates.update({j[0] : 0})
                # Remove the pobability of j
                probabilities.update({j[0] : [-1, -1]}) # do not change !!!
                # Save j in the current solution
                currentSolution["number"].append(j[0])
                currentSolution["value"] += objects[j[0]][0]
                currentSolution["weight"] += objects[j[0]][1]
                # Put j in the current item
                current = j[0]
                # Incrase item check
                cantGo += 1
                # If we found the item we don't need to check the others
                break
        
        # While we didin't check all items
        while cantGo<=n:
            # Next item
            x = random.random()
            # Update probabilities for the current item
            setProb(probabilities,phero,objects,candidates,current)
            for j in probabilities.items():
                # Get the next item
                if x >= j[1][0] and x < j[1][1] and (currentSolution["weight"]+objects[j[0]][1]) <= wmax:
                    # Remove j of candidates
                    candidates.update({j[0] : 0})
                    # Remove the probability of j
                    probabilities.update({j[0] : [-1, -1]}) # do not change !!!
                    # Save j in the current item
                    currentSolution["number"].append(j[0])
                    currentSolution["value"] += objects[j[0]][0]
                    currentSolution["weight"] += objects[j[0]][1]
                    # Put j in the current item
                    current = j[0]
                    # Incrase item check
                    cantGo += 1
                    # If xe found the item we don't need to check the others
                    break
                # If the items is too heavy
                elif (currentSolution["weight"]+objects[j[0]][1]) > wmax :
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
    sorted = bestSolution["number"]
    sorted.sort()
    print(sorted)
    print(f"{bestSolution['value']}\nweith : {bestSolution['weight']}/{wmax}\ntime : {end_process-start_process}\n")

if __name__=="__main__":
    try :
        # Get file name and check if exist --------------------
        print("\nTo quit : CTRL-C")
        name = input("File name : ")
        
        # Load file data --------------------------------------
        with open(name, "r") as f :
            allFile = f.read()
            line = allFile.split("\n")
            
        # Split file data -------------------------------------
        line = line[:-2] # Don't take last line (the solution)
        nb, w = line[0].split()
        n = int(nb)   # Number of items
        wmax = int(w) # Max Weight 
        line = line[1:] # Don't take first line (n, wmax)

        objects = {}
        i = 0
        for l in line :
            # Put all objects in 'objects'
            value, w = l.split()
            i+=1
            objects.update({i : [int(value),int(w)]})

        nbAnts = int(input("How many ants : "))

        ant(objects,nbAnts)
        
    except KeyboardInterrupt:
        """ To stop the program ! """
        print("\nBye !")
        quit()
    except FileNotFoundError:
        """ If file not exist ! """
        print("The file doesn't exist !\nBye !\n")
        quit()
