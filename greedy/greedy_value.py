import time
from operator import itemgetter

def greedy_value(lo, w):
    start_process = time.time()


    #Short life time list to prevent losing info
    lot = lo
    #Current availabilty of the knapsack
    cw = w

    #Current list of object inside the knapsack
    loiks = []

    #Final value of the knapsack
    fv = 0

    #New version Sorting with itemgetter to make it faster than lambda x : x[0]
    lot = sorted(lot,key=itemgetter(0), reverse=True)


    for i in range (0,len(lot)):
        if(cw - int(lot[i][1]) > 0):
            cw -= int(lot[i][1])
            fv += int(lot[i][0])
            loiks.append(lot[i])
        else :
            break

    end_process = time.time()

    return (end_process - start_process), loiks, fv