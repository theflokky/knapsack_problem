# Brute Force Algorithm

# Libraries
import time

# Global Variables
solution = [0, 0, []]

# Functions

# Function wich is calculating all the possibilities of combination of element and returned a list of 0 and 1


def generateAllPossibilities(n):
    l = [[0], [1]]
    start = 0
    for i in range(1, n):
        tmp = len(l)
        for element in l[start:]:
            l.append([0] + element)
            l.append([1] + element)
        start = tmp
    return l[start:]

# Function principal of the bruteForve


def bruteForce(maxWeigth, objectList):
    # We launch the timer
    startTime = time.time()

    # We generate all the possibilities
    allPossibilities = generateAllPossibilities(len(objectList))

    # Initialization of the current best solution
    currentBest = (0, 0)

    # We parcour all the possibilities
    for currentPossibility, element in enumerate(allPossibilities):
        # Initialization of the current Weigth and Value
        currentWeigth = 0
        currentValue = 0

        # We parcours the possibility list
        for index, bit in enumerate(element):
            # If equals to 1
            if bit:
                # We update the currentWeigth
                currentWeigth += objectList[index][1]
                # We verify that the current Solution can enter into the knapsack
                if currentWeigth <= maxWeigth:
                    currentValue += objectList[index][0]
                # If not we pass to next one
                else:
                    break
        # We verify if the current solution is better than the actual better one
        if currentValue > currentBest[1]:
            currentBest = (currentPossibility, currentValue)

    # Ending the timer
    endTime = time.time()

    # Reconstitution of the knapsack in order to facilitate the displaying
    finalKnapsack = []
    for i, obj in enumerate(allPossibilities[currentBest[0]]):
        if (obj == 1):
            finalKnapsack.append(objectList[i])

    return (endTime - startTime), finalKnapsack, currentBest[1]
