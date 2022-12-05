import time


NB_ITEMS = 0
W = 0

finalWeight = 0
finalValue = 0
finalSolution = []
tempSolution = []


# function solving knapsack problems using a branch and bound method
# input : number of items, maximum weight, item list
# output : execution time, solution item list, solution value
def banchBound(nbItems, w, listItems) :
    global NB_ITEMS, W, finalSolution, tempSolution

    NB_ITEMS = nbItems
    W = w

    currentValue = 0
    currentWeight = 0
    i = 0 # index of item

    # start for execution time
    start = time.time()

    # sort items by value/weight
    listItems = sorted(listItems, key= lambda x : -x[0]/x[1])
    
    # initialisation
    while len(tempSolution) < NB_ITEMS:
        tempSolution.append(0)

    # call of the recursive function
    banchBoundRec(listItems,currentValue, currentWeight, 0)

    # preparing returned data
    finalItems = []
    for i in range(len(listItems)):
        if (finalSolution[i] == 1):
            finalItems.append(listItems[i])

    # end for execution time
    end = time.time()


    return (end - start), finalItems, finalValue



# recursive function which for each item of the list, tests to take it or not in order to find the best solution.
# input : item list, current value, current weight, current index item
# output : fill finalWeight, finalValue, finalSolution
def banchBoundRec(listItems, currentValue, currentWeight, i) :
    global NB_ITEMS, W, finalWeight, finalValue, finalSolution, tempSolution


    # if the current item i can be taken
    if(currentWeight + listItems[i][1] <= W):

        tempSolution[i] = 1 # we take this item

        # if the current item is not the last item, we continue with the following item
        if(i < NB_ITEMS-1):
            banchBoundRec(listItems, currentValue + listItems[i][0], currentWeight + listItems[i][1], i+1)

        # if it is the last item and the current value is better than the final value, we save the current solution
        if((i == NB_ITEMS-1) and (currentValue + listItems[i][0] > finalValue)) :
            finalValue = currentValue + listItems[i][0]
            finalWeight = currentWeight + listItems[i][1]
            finalSolution = tempSolution.copy()

            

    # if the following items can lead to a better solution
    if (bound(listItems, currentValue, currentWeight, i) >= finalValue) :

        tempSolution[i] = 0 # we don't take the current item

        # if the current item is not the last item, we continue with the following item
        if(i < NB_ITEMS-1) :
            banchBoundRec(listItems, currentValue, currentWeight, i+1)

        # if it is the last item and the current value is better than the final value, we save the current solution
        if((i == NB_ITEMS-1) and (currentValue > finalValue)) :
            finalValue = currentValue
            finalWeight = currentWeight
            finalSolution = tempSolution.copy()





# function calculating the maximum reachable value with the following items. Works because the items are sorted by value/weight.
# input : item list, temporary solution value, final solution value
# output : maximum reachable value with the following items
def bound(listItems, currentValue, currentWeight, i) :
    global NB_ITEMS, W, finalWeight, finalValue
    v = currentValue
    w = currentWeight

    # iterates through the next items in the list
    for j in range(i+1, NB_ITEMS) :

        # if the item can be taken, we take it
        if (w + listItems[j][1] <= W):
            w = w + listItems[j][1]
            v = v + listItems[j][0]

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
        
    # read the number of item and the capacity of the knapsack
    nbo, ksc = line[0].split()

    # read each line and fill the item list
    listItems = [] 
    for i in range(1, int(nbo)+1):
        oval, owei = line[i].split()
        listItems.append((int(oval), int(owei)))
    else :
        print("Finished loading the items !\n")

    # call the branch and bound function
    temps, finalItems, finalValue = banchBound(int(nbo), int(ksc), listItems)

    # print returned values
    print(finalItems)
    print("final value :", finalValue)

    print("\ntime :", temps)






    
        
        
        
        
        