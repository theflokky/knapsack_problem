import os
import time
import greedy.greedy_value as greedyV
import greedy.greedy_weight as greedyW
import greedy.greedy as greedy
import ant_colony.ant_colony as ant
import brute_force.brute_force as bruteForce


if __name__ == "__main__":
    # Welcome to the programm
    print("Hello and welcome to the knapsack solver !\n")

    low_dimensional = []
    large_scale = []
    multiple_knapsack = []
    mkp_chubeas = []
    chubeas_files = []
    mkp_gk = []
    mkp_sac94 = []

    # Filling the tables with our test files :

    # 0/1 knapsack
    for f in os.listdir("test_files/low-dimensional"):
        low_dimensional.append(os.path.join("test_files/low-dimensional", f))

    for f in os.listdir("test_files/large_scale"):
        large_scale.append(os.path.join("test_files/large_scale", f))

    # Multiple knapsack

    for f in os.listdir("test_files/multiple_knapsack"):
        multiple_knapsack.append(os.path.join(
            "test_files/multiple_knapsack", f))

    for f in os.listdir("test_files/All-MKP-Instances/chubeas"):
        mkp_chubeas.append(os.path.join(
            "test_files/All-MKP-Instances/chubeas", f))

    for f in os.listdir("test_files/All-MKP-Instances/gk"):
        mkp_gk.append(os.path.join("test_files/All-MKP-Instances/gk", f))

    # Main reading loop
    valid = True
    print("If you want to quit you can write 'q'.\n")
    while valid:
        file = None
        try:
            # Here we take the input of the user for which dataset we work with
            file_mode = input(
                "Please enter a value as follow :\n\t-enter \'1\': 0/1 Knapsack problem\n\t-enter \'2\' :  multidimensional problem\n")
            match file_mode:
                # The user wants to quit
                case "q":
                    print("Exiting process, goodbye !")
                    valid = False
                    break
                # If he asks for 0/1 knapsack problem
                case "1":

                    # We're asking for which type of datasets he wishes to use
                    dim = input(
                        "Which scale do you wish to work on ? :\n\t-enter \'1\' : low-dimensional\n\t-enter \'2\' : Large-scale\n")

                    match dim:
                        # As always in case user wants to use
                        case "q":
                            print("Exiting process, goodbye !")
                            valid = False
                            break

                        # Low-dimensional files
                        case "1":
                            # Showcasing all available files
                            i = 0
                            print("Choose which file you want to work on :")
                            for f in low_dimensional:
                                print(f"\'{i}\' : {f}")
                                i += 1
                            num_file = input()
                            # Just in case he wants to quit now
                            if (num_file == "q" or num_file == "Q"):
                                print("Exiting process, goodbye !")
                                valid = False
                                break
                            # Checking if the value processed is numeric
                            if num_file.isnumeric():
                                # Checking if it is included between awaited value
                                # If not then we proceed with default file (the first one)
                                if int(num_file) > i or int(num_file) < 0:
                                    print(
                                        "Invalid option entered, going with the first file by default")
                                    file = low_dimensional[0]
                                else:
                                    file = low_dimensional[int(num_file)]
                            else:
                                print(
                                    "Unknown value detected, please try again. You can exit by pressing 'q'.\n")

                        # Large-scale files
                        case "2":
                            # Showcasing all available files
                            i = 0
                            print("Choose which file you want to work on :")
                            for f in large_scale:
                                print(f"\'{i}\' : {f}")
                                i += 1
                            num_file = input()
                            # In case user wants to quit
                            if (num_file == "q" or num_file == "Q"):
                                print("Exiting process, goodbye !")
                                valid = False
                                break
                            # Checking if the gotten value is numeric
                            if num_file.isnumeric():
                                # Checking if it is included between awaited value
                                # If not then we proceed with default file (the first one)
                                if int(num_file) > i or int(num_file) < 0:
                                    print(
                                        "Invalid option entered, going with the first file by default")
                                    file = large_scale[0]
                                else:
                                    file = large_scale[int(num_file)]
                            else:
                                print(
                                    "Unknown value detected, please try again. You can exit by pressing 'q'.\n")
                        # The user did not input a valid dimensional constraint
                        case _:
                            print(
                                "Unknow value detected, please try again. If you want to quit you can write 'q'.\n")

                # The user asks for multidimensional knapsack
                case "2":
                    
                    # Asking the user which dataset he wants to use
                    dim = input(
                        "Which dataset do you wish to work on ? :\n\t-enter \'1\' : chubeas\n\t-enter \'2\' : gk\n\t-enter \'3\' : sac94\n")

                    # Checking validity of selected input
                    match dim:

                        # The user asked for chubeas
                        case "1":
                            i = 0
                            for f in mkp_chubeas:
                                print(f"\'{i}\' : {f}")
                                i += 1
                            rep_choice = input()
                            # In case user wants to leave now
                            if (rep_choice == "q" or rep_choice == "Q"):
                                print("Exiting process, goodbye !")
                                valid = False
                                break
                            # We check if the user answered a valid input as needed to chose the right file
                            if rep_choice.isnumeric():
                                # Checking if it is included between awaited value
                                # If not then we proceed with the first repository
                                if int(rep_choice) > i or int(rep_choice) < 0:
                                    print(
                                        "Invalid option entered, going with the first repository by default")
                                    rep = mkp_chubeas[0]
                                else:
                                    rep = mkp_chubeas[int(rep_choice)]

                                # We ask for which file in that repository the user will work with
                                j = 0
                                for f in os.listdir(rep):
                                    chubeas_files.append(os.path.join(rep, f))
                                    print(f"\'{j}\' : {chubeas_files[j]}")
                                    j += 1
                                num_file = input()
                                # One more time if the user wants to quit for no reason here, he can
                                if (num_file == "q" or num_file == "Q"):
                                    print("Exiting process, goodbye !")
                                    valid = False
                                    break
                                # Here we check for the value entered by user
                                if num_file.isnumeric():
                                    # Checking if it is included between awaited value
                                    # If not then we proceed with default file (the first one)
                                    if int(num_file) > j or int(num_file) < 0:
                                        print(
                                            "Invalid option entered, going with the first file by default")
                                        file = chubeas_files[0]
                                    else:
                                        file = chubeas_files[int(num_file)]
                                # The user wrote an invalid input
                                else:
                                    print(
                                        "Unknown value detected, please try again. You can exit by pressing 'q'.\n")

                            else:
                                print(
                                    "Unknown value detected, please try again. You can exit by pressing 'q'.\n")

                        # The user asked for gk
                        case "2":
                            i = 0
                            for f in mkp_gk:
                                print(f"\'{i}\' : {f}")
                                i += 1
                            num_file = input()
                            # What if the user wants to quit ? Well he can
                            if (num_file == "q" or num_file == "Q"):
                                print("Exiting process, goodbye !")
                                valid = False
                                break
                            # Checking the value of the input
                            if num_file.isnumeric():
                                # Checking if it is included between awaited value
                                # If not then we proceed with default file (the first one)
                                if int(num_file) > i or int(num_file) < 0:
                                    print(
                                        "Invalid option entered, going with the first file by default")
                                    file = mkp_gk[0]
                                else:
                                    file = mkp_gk[int(num_file)]
                            # Invalid input
                            else:
                                print(
                                    "Unknown value detected, please try again. You can exit by pressing 'q'.\n")

                        # The user asked for sac94
                        case "3":
                            print("To do, i'm sorry this one isn't done")

                        # The user wrote an invalid input
                        case _:
                            print(
                                "Unknown value detected, please try again. You can exit by pressing 'q'.\n")

                # The user inputs an invalid value
                case _:
                    print(
                        "Non recognized value was written, please try again. If you want to quit you can write 'q'.\n")

            if file != None:
                # Checking if with which version we work, this changes the type of file

                if file_mode == "1":
                    # Reading the data of 0/1 problem
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
                    # We will collect the data
                    # First with the number of object and the capacity of the knapsack
                    nbo, ksc = line[0].split()
                    n = int(nbo)  # number of object
                    wmax = int(ksc)  # Maximum weight
                    # Proceeding every object and giving the time needed to process the file
                    list_objects = []
                    for i in range(1, n+1):
                        oval, owei = line[i].split()
                        list_objects.append((int(oval), int(owei)))
                    else:
                        end_reading = time.time()
                        print("Finished loading the objects !\n")
                        print(
                            f"The reading process took : {end_reading - start_reading} s !\n")
                    # Check up temporaire, à retirer un jour
                    print(list_objects)
                    print("\n")
                    # We ask which algorithm you want to run
                    algo = input("Which algorithm do you wish to run this data set on ?\nAvailable algorithms are :\n\tGreedy by value : \"gbv\"\n\tGreedy by weight : \"gbw\"\n\tGreedy : \"greed\"\n\tAnt algorithm : \"ant\"\n\tBrute Force : \"bf\"\nPlease enter your selection by writing the code next to the algorithm of your choice...\n")
                    match algo:
                        # Going with the greedy by value algorithm
                        case "gbv":
                            print("Processing data sets with \"Greedy by value\"")
                            timer, final_knapsack, final_value = greedyV.greedy_value_01(list_objects, wmax)
                            print(
                                f"The process took : {timer}s for execution\nThe knapsack contains these objects : {final_knapsack}\nFor a value of : {final_value}")
                        # Going with the greedy by weight algorithm
                        case "gbw":
                            print("Processing data sets with \"Greedy by weight\"")
                            timer, final_knapsack, final_value = greedyW.greedy_weight_01(list_objects, wmax)
                            print(
                                f"The process took : {timer}s for execution\nThe knapsack contains these objects : {final_knapsack}\nFor a value of : {final_value}")
                        # Going with the greedy algorithm
                        case "greed":
                            print("Processing data sets with \"Greedy\"")
                            timer, final_knapsack, final_value = greedy.greedy_01(list_objects, wmax)
                            print(
                                f"The process took : {timer}s for execution\nThe knapsack contains these objects : {final_knapsack}\nFor a value of : {final_value}")
                        # Going with the ant algorithm
                        case "ant":
                            print("Processing data sets with \"Ant algorithm\"")
                            nbAnts = int(input("How many ants : "))
                            timer, final_knapsack, final_value = ant.ant(list_objects, nbAnts, n, wmax)
                            print(
                                f"The process took : {timer}s for execution\nThe knapsack contains these objects : {final_knapsack}\nFor a value of : {final_value}")
                        case "bf":
                            timer, final_knapsack, final_value = bruteForce.bruteForce(wmax, list_objects)
                            print(
                                f"The process took : {timer}s for execution\nThe knapsack contains these objects : {final_knapsack}\nFor a value of : {final_value}")
                        case _:
                            print(
                                "Unknown value was inputed, please try again. To quit press 'q'\n")

                elif file_mode == "2":
                    # Reading the data of multidimensional
                    # this means the file looks up like that :
                    #
                    # Number of objects Number of dimension (M) Optimal solution (0 if none) 
                    # 
                    # P1 W1D1 W1D2 ... W1DM
                    #    . . .
                    # Pn WnD1 WnD2 ... WnDM
                    #
                    # With Pn the profit (value) of the object
                    # and WnDM the weight in the M dimension for this object
                    #
                    
                    # Let's read the file
                    print("Starting reading the file !")
                    start_reading = time.time()
                    with open(file, "r") as f:
                        data = f.read()
                        line = data.split("\n")

                    # Starting to gather data
                    nbo, ndim, opti_sol = line[0].split()

                    n = int(nbo)
                    ndim = int(ndim)
                    ksc = []
                    # In order to gather one object at a time
                    object = []

                    # Receiving container
                    list_objects = []

                    # Checking all objects
                    acc = 0
                    for l in line[1:]:
                        # getting all objects and their profit
                        if len(list_objects) < n:
                            for w in l.split():
                                object.append(int(w))
                                acc+=1
                                if acc == ndim+1:
                                    list_objects.append(object)
                                    acc = 0
                                    object = []
                        else:
                            # Getting the knapsack capacity             
                            for w in l.split():    
                                ksc.append(int(w))

                    # We ask which algorithm you want to run
                    algo = input("Which algorithm do you wish to run this data set on ?\nAvailable algorithms are :\n\tGreedy by value : \"gbv\"\n\tGreedy by weight : \"gbw\"\n\tGreedy : \"greed\"\n\tAnt algorithm : \"ant\"\n\tBrute Force : \"bf\"\nPlease enter your selection by writing the code next to the algorithm of your choice...\n")
                    match algo:
                        # Going with the greedy by value algorithm
                        case "gbv":
                            print("Processing data sets with \"Greedy by value\"")
                            timer, final_knapsack, final_value = greedyV.greedy_value_multi(list_objects, ksc)
                            print(
                                f"The process took : {timer}s for execution\nThe knapsack contains these objects : {final_knapsack}\nFor a value of : {final_value}")
                        # Going with the greedy by weight algorithm
                        case "gbw":
                            print("Processing data sets with \"Greedy by weight\"")
                            timer, final_knapsack, final_value = greedyW.greedy_weight_multi(list_objects, ksc)
                            print(
                                f"The process took : {timer}s for execution\nThe knapsack contains these objects : {final_knapsack}\nFor a value of : {final_value}")
                        # Going with the greedy algorithm
                        case "greed":
                            print("Processing data sets with \"Greedy\"")
                            timer, final_knapsack, final_value = greedy.greedy_multi(list_objects, ksc)
                            print(
                                f"The process took : {timer}s for execution\nThe knapsack contains these objects : {final_knapsack}\nFor a value of : {final_value}")
                        # Going with the ant algorithm
                        case "ant":
                            print("If someone as enought faith or it")
                            #print("Processing data sets with \"Ant algorithm\"")
                            #nbAnts = int(input("How many ants : "))
                            #timer, final_knapsack, final_value = ant.ant(list_objects, nbAnts, n, wmax)
                            #print(
                            #    f"The process took : {timer}s for execution\nThe knapsack contains these objects : {final_knapsack}\nFor a value of : {final_value}")
                        case "bf":
                            print("Will it be developped on day ?")
                            timer, final_knapsack, final_value = bruteForce.bruteForceMultiDimensional(ksc, list_objects)
                            print(
                                f"The process took : {timer}s for execution\nThe knapsack contains these objects : {final_knapsack}\nFor a value of : {final_value}")
                        case _:
                            print(
                                "Unknown value was inputed, please try again. To quit press 'q'\n")

                # If not looping back to input questions

        # Special features for Pierre
        except KeyboardInterrupt:
            # Quitting programs anytime, anyway you want
            print("\n Quit by force, bye !")
            break
