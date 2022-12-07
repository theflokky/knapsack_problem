import time

def dynamic(lo, w):
    start_process = time.time()

    lot = lo[:]

    loiks = []
    fv = 0

    # Creating a table consisting of 0 to n objects as rows
    # and 0 to Knapsack maximum weight as columns
    matrix = [[0 for i in range(w + 1)] for i in range(len(lot) + 1)]

    # Filling up the table
    for i in range(len(lot)+1):
        for j in range(w+1):
            # used for setting the 0th row and 0th column to 0
            if i == 0 or j == 0:
                matrix[i][j] = 0
            # Checking if weight of ith item is acceptable
            elif lot[i-1][1] <= j:
                # Selecting the best value out of two possibilities
                # matrix[i-1][j] means the item isn't included
                # lot[i-1][0] means the item is included
                matrix[i][j] = max(lot[i-1][0] + matrix[i-1][j - lot[i-1][1]], matrix[i-1][j])
            else :
                # Objects weigth excesseded maximum capacity
                matrix[i][j] = matrix[i-1][j]

    fv = matrix[len(lot)][w]
    checking_value = fv
    checking_weigth = w

    # Getting all selected objects
    for i in range(len(lot), 0, -1):
        # When reached all selected item are found
        if checking_value <= 0:
            break
        
        if checking_value == matrix[i-1][checking_weigth]:
            # The item wasn't included so we don't do anything
            continue
        else :
            # This item is used, so we load it in loiks
            loiks.append(lot[i-1])

            # As it was selected we need to substract the weigth and value from the checkers
            checking_value -= lot[i-1][0]
            checking_weigth -= lot[i-1][1]



    end_process = time.time()

    return (end_process - start_process), loiks, fv
    