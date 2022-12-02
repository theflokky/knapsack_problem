#pip install matplotlib
#pip install scipy

import sys
import matplotlib.pyplot as plt


title = "Comparison of the Execution Time of some algorithms\nresolving knackpack problems"
xLabel = "Test Data"
yLabel = "Execution Time (s)"
personalAlgo = "'Personal Algorithm'"


def graph(time, tests):

    print("\n brute_force :     ", time["brute_force"], "\n branch_and_bound :", time["branch_and_bound"], "\n greedy :          ", time["greedy"], "\n greedy_value :    ", time["greedy_value"], "\n greedy_weight :   ", time["greedy_weight"], "\n dynamic :         ", time["dynamic_programming"], "\n polynomial :      ", time["polynomial"], "\n grasp :           ", time["grasp"], "\n ant_colony :      ", time["ant_colony"], "\n personal :        ", time["personal"], "\n\n test files :      ", tests, flush=True)
    print()


    
    if len(time["brute_force"]) != 0 :
        plt.plot(tests, time["brute_force"], label='Brute force', marker = '.', color = 'royalblue')
    
    if len(time["branch_and_bound"]) != 0 :
        plt.plot(tests, time["branch_and_bound"], label='Banch and bound', marker = '.', color = 'orange')
    
    if len(time["greedy"]) != 0 :
        plt.plot(tests, time["greedy"], label = 'Greedy', marker = '.', color = 'limegreen')

    if len(time["greedy_value"]) != 0 :
        plt.plot(tests, time["greedy_value"], label = 'Greedy Value', marker = '.', color = 'tan')

    if len(time["greedy_weight"]) != 0 :
        plt.plot(tests, time["greedy_weight"], label = 'Greedy Weight', marker = '.', color = 'peachpuff')

    if len(time["dynamic_programming"]) != 0 :
        plt.plot(tests, time["dynamic_programming"], label = 'Dynamic', marker = '.', color = 'r')
    
    if len(time["polynomial"]) != 0 :
        plt.plot(tests, time["polynomial"], label = 'Polynomial', marker = '.', color = 'm')
    
    if len(time["grasp"]) != 0 :
        plt.plot(tests, time["grasp"], label = 'Grasp', marker = '.', color = 'c')
    
    if len(time["ant_colony"]) != 0 :
        plt.plot(tests, time["ant_colony"], label = 'Ant colony', marker = '.', color = 'hotpink')

    if len(time["personal"]) != 0 :
        plt.plot(tests, time["personal"], label = personalAlgo, marker = '.', color = 'y')

    plt.grid()
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)

    plt.title(title, fontname = "Times New Roman", fontsize = 15, fontweight = "bold", y = 1.01)

    plt.legend()
    plt.show()

    
