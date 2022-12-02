import time


NB_ITEMS = 0
W = 0

finalWeight = 0
finalValue = 0
finalSolution = []
tempSolution = []


def banchBound(nbObjects, w, listObjects) :
    global NB_ITEMS, W, finalSolution, tempSolution

    NB_ITEMS = nbObjects
    W = w

    currentValue = 0
    currentWeight = 0
    i = 0 # index of item

    # start for execution time
    start = time.time()

    # sort items by value/weight
    listObjects = sorted(listObjects, key= lambda x : -x[0]/x[1])
    
    # initialisation
    while len(tempSolution) < NB_ITEMS:
        tempSolution.append(0)

    # call of the recursive function
    banchBoundRec(listObjects,currentValue, currentWeight, 0)

    # preparing returned data
    finalObjects = []
    for i in range(len(listObjects)):
        if (finalSolution[i] == 1):
            finalObjects.append(listObjects[i])

    # end for execution time
    end = time.time()


    return (start - end), finalObjects, finalValue



    
# description
def banchBoundRec(listObjects, currentValue, currentWeight, i) :
    global NB_ITEMS, W, finalWeight, finalValue, finalSolution, tempSolution


    # if the current object i can be taken
    if(currentWeight + listObjects[i][1] <= W):

        tempSolution[i] = 1 # we take this object

        # if the current object is not the last item, we continue with the following item
        if(i < NB_ITEMS-1):
            banchBoundRec(listObjects, currentValue + listObjects[i][0], currentWeight + listObjects[i][1], i+1)

        # if it is the last object and the current value is better than the final value, we save the current solution
        if((i == NB_ITEMS-1) and (currentValue + listObjects[i][0] > finalValue)) :
            finalValue = currentValue + listObjects[i][0]
            finalWeight = currentWeight + listObjects[i][1]
            finalSolution = []
            for j in tempSolution :
                finalSolution.append(j)

            
    
    if (bound(listObjects, currentValue, currentWeight, i) >= finalValue) :
        tempSolution[i] = 0

        if(i < NB_ITEMS-1) :
            banchBoundRec(listObjects, currentValue, currentWeight, i+1)

        if((currentValue > finalValue) and (i == NB_ITEMS-1)) :
            finalValue = currentValue
            finalWeight = currentWeight
            finalSolution = []
            for j in tempSolution :
                finalSolution.append(j)





def bound(listObjects, currentValue, currentWeight, i) :
    global NB_ITEMS, W, finalWeight, finalValue
    v = currentValue
    w = currentWeight
    for j in range(i+1, NB_ITEMS) :
        if (w + listObjects[j][1] <= W):
            w = w + listObjects[j][1]
            v = v + listObjects[j][0]
    return v










if __name__=="__main__":
    file = input("file name : ")

    with open(file, "r") as f:
        data = f.read()
        line = data.split("\n")
        
    # First with the number of object and the capacity of the knapsack
    nbo, ksc = line[0].split()

    # Proceeding every object and giving the time needed to process the file
    listObjects = [] 
    for i in range(1, int(nbo)+1):
        oval, owei = line[i].split()
        listObjects.append((int(oval), int(owei)))
    else :
        print("Finished loading the objects !\n")


    temps, finalObjects, finalValue = banchBound(int(nbo), int(ksc), listObjects)

    print(finalObjects)
    print("final value :", finalValue)

    print("\ntemps :", temps)






    
        
        
        
        
        