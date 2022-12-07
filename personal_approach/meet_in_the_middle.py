import time 
import brute_force.brute_force as brute_force

def solveSubSet(l, w):

    no_use, optimal_sac, optimal_value = brute_force.bruteForce(w, l)

    return optimal_sac, optimal_value



def meet_in_the_middle(lo, w):

    # We first need to split our array in two
    start_process = time.time()

    lot = lo[:]

    mid = int(len(lot)/2)


    left, right = [], []


    for i in range(mid):
        left.append(lot[i])

    for i in range(mid, len(lot)):
        right.append(lot[i])

    left_sac, left_value  =  solveSubSet(left, w)
    right_sac, right_value = solveSubSet(right, w)


    # merging right into left if possible
    cw = 0
    loiks = left_sac[:]
    fv = left_value
    for i in loiks:
        cw += i[1]

    for i in right_sac:
        if cw + i[1] <= w:
            loiks.append(i)
            fv += i[0]
            cw += i[1]

    


    end_process = time.time()

    return (end_process - start_process), loiks, fv 
