"""
Brute Force Algorithm Implementation.
"""

#Imports
import time

###FUNCTION DECLARATIONS###

def generateAllPossibilities(n):
    """
    Returns a list containing every sequence of n bits possible.
    A 1 in position number i indicates that the object number i must be taken.
    A 0 in position number i indicated that the object number i shall not be taken.
    Parameters :
    \tn : int
    Output :
    \tl : list<list<int>>
    Example :
    >>> brute_force.generateAllPossibilities(3)
    [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0], [0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]]
    """
    l = [[0], [1]]
    start = 0
    for i in range(1, n):
        tmp = len(l)
        for element in l[start:]:
            l.append([0] + element)
            l.append([1] + element)
        start = tmp
    return l[start:]

def bruteForce(maxWeight, objectList):
    """
    Main function implementing the Brute Force Algorithm.
    Returns the time used for the execution, a list containing the objects taken and the optimal solution, given maxWeight the maximum weight of the knapsack and objectList, a list describing the set of objects that should be considered.
    Parameters :
    \tmaxWeight : int
    \tobjectList : list<(int,int)>
    Ourput :
    \t((runTime, finalKnapsack, solution) : (float, list<(int,int)>, list<int>)
    """

    # Starting timer
    startTime = time.time()

    # Generation of possibilities in an exhaustive list
    allPossibilities = generateAllPossibilities(len(objectList))

    # Initialization of the current best solution
    currentBest = (0, -1)

    # Going through every possibility
    for currentPossibility, element in enumerate(allPossibilities):
        # Initialization of the current Weight and Value
        # currentWeight in the bag
        # currentValue in the bag
        currentWeight = 0
        currentValue = 0

        # Going through the bits encoded by the possibility
        for index, bit in enumerate(element):
            # If the bit is a 1
            if bit:
                # Update of currentWeight
                currentWeight += objectList[index][1]
                # Verification that currentWeight doesn't exceed maxWeight
                if currentWeight <= maxWeight:
                    currentValue += objectList[index][0]
                # If it exceeds, this possibility isn't feasible. We go to the next one
                else:
                    break
        # If the currentPossibility is better than the previous best one
        if currentValue > currentBest[1]:
            # The currentBest is updated
            currentBest = (currentPossibility, currentValue)

    # Ending the timer
    endTime = time.time()

    # Reconstitution of the knapsack for displaying purposes
    finalKnapsack = []
    for i, obj in enumerate(allPossibilities[currentBest[0]]):
        if (obj == 1):
            finalKnapsack.append(objectList[i])

    return ((endTime - startTime), finalKnapsack, currentBest[1])

def initializationOfList(size, list):
    for i in range(size):
        list.append(0)
    return list

def bruteForceMultiDimensional(ksc, objectList):
    """
    Main Function implementing the Brute Force Algorihm on the MultiDimensional Knapsack Problem.
    
    """
    print(ksc)
    # Starting timer
    startTime = time.time()

    nbDimension = len(ksc)

    currentBest = (0, -1)


    #Generate All Possibilities
    allPossibilities = generateAllPossibilities(len(objectList))


    #parcours de toutes les possibilités
    for currentPossibility, possibility in enumerate(allPossibilities):
        currentWeight = initializationOfList(nbDimension, [])
        currentValue = 0

        for index, bit in enumerate(possibility):
            exit = 0
            alreadyAdded = 0
            #We add the object to the list
            for dimension in range(nbDimension):
                if bit:
                    currentWeight[dimension] += objectList[index][dimension+1]

                    #cela rentre dans le sac
                    if(currentWeight[dimension] <= ksc[dimension]):
                        if(alreadyAdded == 0):
                            currentValue += objectList[index][0]
                            alreadyAdded = 1
                    else:
                        exit=1
                        break
            if(exit == 1):
                break
                    

        if (currentValue > currentBest[1]):
            currentBest = (currentPossibility, currentValue)
        
        
    # Ending the timer
    endTime = time.time()

    # Reconstitution of the knapsack for displaying purposes
    finalKnapsack = []
    for i, obj in enumerate(allPossibilities[currentBest[0]]):
        if (obj == 1):
            finalKnapsack.append(objectList[i])

    return ((endTime - startTime), finalKnapsack, currentBest[1])

    
            
                


            