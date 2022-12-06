#pip install matplotlib
#pip install scipy
#sudo apt-get install python3-pil python3-pil.imagetk
#sudo apt install msttcorefonts -qq

import sys
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# label names
title = "Comparison of the Execution Time of some algorithms\nfor solving Knapsack Problems."
xLabel = "Tested Data"
yLabel = "Execution Time (seconds)"
personalAlgo = "'Personal Algorithm'"


# create and show the graph
def graph(time, tests):

    # print the data in terminal
    print("\n brute_force :     ", time["brute_force"], flush=True)
    print(" branch_and_bound :", time["branch_and_bound"], flush=True)
    print(" greedy :          ", time["greedy"], flush=True)
    print(" greedy_value :    ", time["greedy_value"], flush=True)
    print(" greedy_weight :   ", time["greedy_weight"], flush=True)
    print(" dynamic :         ", time["dynamic_programming"], flush=True)
    print(" polynomial :      ", time["polynomial"], flush=True)
    print(" grasp :           ", time["grasp"], flush=True)
    print(" ant_colony :      ", time["ant_colony"], flush=True)
    print(" personal :        ", time["personal"], flush=True)
    print("\n test files :      ", tests, "\n", flush=True)


    # create a curve for each tested algorithm
    
    if len(time["brute_force"]) != 0 :
        plt.plot(tests, time["brute_force"], label='Brute force', marker = '.', color = 'royalblue')
    
    if len(time["branch_and_bound"]) != 0 :
        plt.plot(tests, time["branch_and_bound"], label='Banch and bound', marker = '.', color = 'orange')
    
    if len(time["greedy"]) != 0 :
        plt.plot(tests, time["greedy"], label = 'Greedy', marker = '.', color = 'limegreen')

    if len(time["greedy_value"]) != 0 :
        plt.plot(tests, time["greedy_value"], label = 'Greedy Value', marker = '.', color = 'yellowgreen')

    if len(time["greedy_weight"]) != 0 :
        plt.plot(tests, time["greedy_weight"], label = 'Greedy Weight', marker = '.', color = 'seagreen')

    if len(time["dynamic_programming"]) != 0 :
        plt.plot(tests, time["dynamic_programming"], label = 'Dynamic', marker = '.', color = 'r')
    
    if len(time["polynomial"]) != 0 :
        plt.plot(tests, time["polynomial"], label = 'Polynomial', marker = '.', color = 'm')
    
    if len(time["grasp"]) != 0 :
        plt.plot(tests, time["grasp"], label = 'Grasp', marker = '.', color = 'skyblue')
    
    if len(time["ant_colony"]) != 0 :
        plt.plot(tests, time["ant_colony"], label = 'Ant colony', marker = '.', color = 'hotpink')

    if len(time["personal"]) != 0 :
        plt.plot(tests, time["personal"], label = personalAlgo, marker = '.', color = 'tan')


    # create labels
    plt.grid()
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.title(title, fontname = "Liberation Serif", fontsize = 15, fontweight = "bold", y = 1.01)
    plt.legend()


    # show graph
    plt.show()

    
