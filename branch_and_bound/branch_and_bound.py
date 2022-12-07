import time


NB_objects = 0
W = 0

finalWeight = 0
finalValue = 0
finalSolution = []
tempSolution = []


# function solving knapsack problems using a branch and bound method
# input : number of objects, maximum weight, object list
# output : execution time, solution object list, solution value
def banchBound(nbobjects, w, listobjects) :
    global NB_objects, W, finalSolution, tempSolution ,finalValue, finalWeight

    NB_objects = nbobjects
    W = w

    finalWeight = 0
    finalValue = 0
    finalSolution = []
    tempSolution = []

    currentValue = 0
    currentWeight = 0
    i = 0 # index of object

    # start for execution time
    start = time.time()

    # sort objects by value/weight
    listobjects = sorted(listobjects, key= lambda x : -x[0]/x[1] if x[1] else -x[0])
    
    # initialisation
    while len(tempSolution) < NB_objects:
        tempSolution.append(0)

    # call of the recursive function
    banchBoundRec(listobjects,currentValue, currentWeight, 0)

    # preparing returned data
    finalobjects = []
    for i in range(len(listobjects)):
        if (finalSolution[i] == 1):
            finalobjects.append(listobjects[i])

    # end for execution time
    end = time.time()


    return (end - start), finalobjects, finalValue



# recursive function which for each object of the list, tests to take it or not in order to find the best solution.
# input : object list, current value, current weight, current index object
# output : fill finalWeight, finalValue, finalSolution
def banchBoundRec(listobjects, currentValue, currentWeight, i) :
    global NB_objects, W, finalWeight, finalValue, finalSolution, tempSolution


    # if the current object i can be taken
    if(currentWeight + listobjects[i][1] <= W):

        tempSolution[i] = 1 # we take this object

        # if the current object is not the last object, we continue with the following object
        if(i < NB_objects-1):
            banchBoundRec(listobjects, currentValue + listobjects[i][0], currentWeight + listobjects[i][1], i+1)

        # if it is the last object and the current value is better than the final value, we save the current solution
        if((i == NB_objects-1) and (currentValue + listobjects[i][0] > finalValue)) :
            finalValue = currentValue + listobjects[i][0]
            finalWeight = currentWeight + listobjects[i][1]
            finalSolution = tempSolution.copy()

            

    # if the following objects can lead to a better solution
    if (bound(listobjects, currentValue, currentWeight, i) >= finalValue) :

        tempSolution[i] = 0 # we don't take the current object

        # if the current object is not the last object, we continue with the following object
        if(i < NB_objects-1) :
            banchBoundRec(listobjects, currentValue, currentWeight, i+1)

        # if it is the last object and the current value is better than the final value, we save the current solution
        if((i == NB_objects-1) and (currentValue > finalValue)) :
            finalValue = currentValue
            finalWeight = currentWeight
            finalSolution = tempSolution.copy()





# function calculating the maximum reachable value with the following objects. Works because the objects are sorted by value/weight.
# input : object list, temporary solution value, final solution value
# output : maximum reachable value with the following objects
def bound(listobjects, currentValue, currentWeight, i) :
    global NB_objects, W, finalWeight, finalValue
    v = currentValue
    w = currentWeight

    # iterates through the next objects in the list
    for j in range(i+1, NB_objects) :

        # if the object can be taken, we take it
        if (w + listobjects[j][1] <= W):
            w = w + listobjects[j][1]
            v = v + listobjects[j][0]

    # return the calculated value
    return v









# to test the program independently of the graphical interface
if __name__=="__main__":

    # asks the user for a file name in terminal
    file = input("file name : ")

    # start to read the file
    with open(file, "r") as f:
        data = f.read()
        line = data.split("\n")
        
    # read the number of object and the capacity of the knapsack
    nbo, ksc = line[0].split()

    # read each line and fill the object list
    listobjects = [] 
    for i in range(1, int(nbo)+1):
        oval, owei = line[i].split()
        listobjects.append((int(oval), int(owei)))
    else :
        print("Finished loading the objects !\n")

    # call the branch and bound function
    temps, finalobjects, finalValue = banchBound(int(nbo), int(ksc), listobjects)

    # print returned values
    print(finalobjects)
    print("final value :", finalValue)

    print("\ntime :", temps)






    
        
        
        
        
        