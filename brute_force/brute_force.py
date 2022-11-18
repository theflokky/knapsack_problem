# Brute Force Algorithm

# Libraries
import time

# Global Variables
solution = [0, 0, []]

# Functions


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


def bruteForce(maxWeigth, objectList):
    startTime = time.time()
    l = generateAllPossibilities(len(objectList))
    current_best = (0, 0)
    for current_possibility, element in enumerate(l):
        current_weight = 0
        current_value = 0
        for index, bit in enumerate(element):
            if bit:
                current_weight += objectList[index][1]
                if current_weight <= maxWeigth:
                    current_value += objectList[index][0]
                else:
                    break
        if current_value > current_best[1]:
            current_best = (current_possibility, current_value)
    endTime = time.time()
    finalKnapsack = []
    for i, obj in enumerate(l[current_best[0]]):
        if (obj == 1):
            finalKnapsack.append(objectList[i])

    return (endTime - startTime), finalKnapsack, current_best[1]
