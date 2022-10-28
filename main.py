import os.path
import time
import greedy.greedy_value as greedy




if __name__=="__main__":
    #Welcome to the programm
    print("Hello and welcome to the knapsack solver !\n")

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


                #We ask which algorithm you want to run
                algo = input("Which algorithm do you wish to run this data set on ?\nAvailable algorithms are :\n\tGreedy by value : \"gbv\"\nPlease enter your selection by writing the code next to the algorithm of your choice...\n")


                # Going with the greedy by value algorithm
                if(algo == "gbv") :
                    print("Processing data sets with \"Greedy by value\"")

                    time, final_knapsack, final_value = greedy.greedy_value(list_objects, wmax)

                    print("The process took : "+str(time)+" s for execution\nThe knapsack contains these objects :"+str(final_knapsack)+"\nFor a value of :"+str(final_value))

            #Looping back to entering a file name
            else:
                print("Your input wasn't an existing file or the path didn't lead to a file")
            