import time

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


    while(cw > 0 and lot) :

        #Most valuable object
        mvo = max(lot)

        lot.remove(mvo)
        if(cw - int(mvo[1]) > 0):
            cw -= int(mvo[1])
            fv += mvo[0]
            loiks.append(mvo)



    end_process = time.time()

    return (end_process - start_process), loiks, fv