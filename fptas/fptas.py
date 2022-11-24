import os.path
import time

def dynamic(wmax :  int, objects : list):
    matrix = [[0 for i in range(wmax + 1)] for i in range(len(objects) + 1)]
    for i in range(len(objects)+1):
        for w in range(wmax+1):
            if i == 0 or w == 0:
                matrix[i][w] = 0
            elif objects[i-1][1] <= w:
                matrix[i][w] = max(objects[i-1][0] + matrix[i-1][w - objects[i-1][1]], matrix[i-1][w])
            else :
                matrix[i][w] = matrix[i-1][w]

    selection = [False for i in range(len(objects))]
    j = wmax
    while j > 0:
        for i in range(len(objects),0,-1):
            if matrix[i][j] > matrix[i-1][j] :
                selection[i-1] = True
                break
        j-=1
    print(selection)
def fptas(epsilon : float, wmax : int, objects : list):

    P = objects[0][0]
    for i in range(1,len(objects)):
        if objects[i][0] > P:
            P = objects[i][0]
    K = epsilon * P / len(objects)
    tmp_objects = [(int(a[0]/K), a[1]) for a in objects]
    dynamic(wmax,tmp_objects)
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
                


