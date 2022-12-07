import os.path
import time

def dynamic(lo, w):
    lot = lo[:]

    loiks = []

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

    checking_value = matrix[len(lot)][w]
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
            # This item is used, so we load it's index in order to know which item we will need to take
            loiks.append(i-1)

            # As it was selected we need to substract the weigth and value from the checkers
            checking_value -= lot[i-1][0]
            checking_weigth -= lot[i-1][1]

    return loiks
    


def fptas(epsilon : float, wmax : int, objects : list):

    start_process = time.time()

    final_value = 0
    final_knapsack = []

    # As the dynamic approach is faster the smaller the values are we try to reduce to values as much as possible
    
    P = objects[0][0]
    # We first get the highest value available
    for i in range(1,len(objects)):
        if objects[i][0] > P:
            P = objects[i][0]
    
    # We then see how much we can divide the profits
    K = epsilon * P / len(objects)

    # We apply our results to the list
    tmp_objects = [(int(a[0]/K), a[1]) for a in objects]

    # This version of dynamic returns the list of index of objects (as the paramater is a modified version) in order to get the final knapsack
    liste_index = dynamic(tmp_objects,wmax)

    for i in liste_index :
        final_knapsack.append(objects[i])
        final_value += objects[i][0]

    end_process = time.time()

    return (end_process - start_process), final_knapsack, final_value


if __name__=="__main__":
    #Main reading loop
    valid = True
    while valid:

        #Here we take the input of the user
        file = input("If you want to quit you can write 'q'.\nPlease enter a filename or a path to a file :...\n")

        #If he wants to quit
        if(file == "q" or file == "Q") :
            print("Exiting process, goodbye !")
            valid = False

        else:
            
            #Checking if the file or path leads to something that exist and it is a file
            if (os.path.exists(file) and os.path.isfile(file)):

                #Reading the data, we consider the user gives the right kind of file for now
                # this means the file looks up like that :
                #
                # Number of items  Capacity of the Knapsack
                # [V1] [W1]
                # ... n-2 objects
                # [Vn] [Wn]
                # With Vn the value and Wn the weight
                #

                print("Starting reading the file !")
                start_reading = time.time()
                with open(file, "r") as f:
                    data = f.read()
                    line = data.split("\n")

                #We will collect the data
                
                # First with the number of object and the capacity of the knapsack
                nbo, ksc = line[0].split()
                
                n = int(nbo) # number of object
                wmax = int(ksc) # Maximum weight

                # Proceeding every object and giving the time needed to process the file
                list_objects = [] 
                for i in range(1, n+1):
                    oval, owei = line[i].split()
                    list_objects.append((int(oval), int(owei)))
                else :
                    end_reading = time.time()
                    print("Finished loading the objects !\n")
                    print(f"The reading process took : {end_reading - start_reading} s !\n")

                #Check up temporaire, à retirer un jour
                print(list_objects)
                print("\n")
                fptas(1, wmax, list_objects)
                


