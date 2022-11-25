import time


NB_ITEMS = 0
W = 0

finalWeight = 0
finalValue = 0
X = []
Y = []


def banchBound(nbObjects, w, list_objects) :
    global NB_ITEMS, W, X

    NB_ITEMS = nbObjects
    W = w

    currentValue = 0
    currentWeight = 0
    i = 0 #index of item

    start = time.time()
    banchBoundRec(list_objects,currentValue, currentWeight, 0)
    end = time.time()

    finalObjects = []
    for i in range(len(X)):
        if (X[i] == 1):
            finalObjects.append(list_objects[i])

    return (start - end), finalObjects, finalValue



    


def banchBoundRec(list_objects, currentValue, currentWeight, i) :
    global NB_ITEMS, W, finalWeight, finalValue, X, Y


    if(currentWeight + list_objects[i][1] <= W):
        Y[i] = 1

        if(i < N_ITEMS-1):
            banchBoundRec(list_objects, currentValue + list_objects[i][0], currentWeight + list_objects[i][1], i+1)

        if((currentValue + list_objects[i][0] > finalValue) and (i == N_ITEMS-1)) :
            finalValue = currentValue + list_objects[i][0]
            finalWeight = currentWeight + list_objects[i][1]
            X = []
            for j in Y :
                X.append(j)

            
            
    if (bound(list_objects, currentValue, currentWeight, i) >= finalValue) :
        Y[i] = 0

        if(i < N_ITEMS-1) :
            banchBoundRec(list_objects, currentValue, currentWeight, i+1)

        if((currentValue > finalValue) and (i == N_ITEMS-1)) :
            finalValue = currentValue
            finalWeight = currentWeight
            X = []
            for j in Y :
                X.append(j)





def bound(list_objects, currentValue, currentWeight, i) :
    global NB_ITEMS, W, finalWeight, finalValue, X, Y
    v = currentValue
    w = currentWeight
    for j in range(i+1, N_ITEMS) :
        if (w + list_objects[j][1] <= W):
            w = w + list_objects[j][1]
            v = v + list_objects[j][0]
    return v










if __name__=="__main__":
    file = input("file name : ")

    with open(file, "r") as f:
        data = f.read()
        line = data.split("\n")
        
    # First with the number of object and the capacity of the knapsack
    nbo, ksc = line[0].split()
        
    N_ITEMS = int(nbo) # number of object
    W = int(ksc) # Maximum weight

    # Proceeding every object and giving the time needed to process the file
    list_objects = [] 
    for i in range(1, N_ITEMS+1):
        oval, owei = line[i].split()
        list_objects.append((int(oval), int(owei)))
    else :
        print("Finished loading the objects !\n")


    

    while len(Y) < N_ITEMS:
        Y.append(0)

    
    list_objects = sorted(list_objects, key= lambda x : -x[0]/x[1])

    temps, finalObjects, finalValue = banchBound(NB_ITEMS, W, list_objects)

    print(finalObjects)
    print("final value :", finalValue)

    print("\ntemps :", temps)






    
        
        
        
        
        