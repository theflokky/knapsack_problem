#pip install matplotlib
#pip install scipy

import sys
import matplotlib.pyplot as plt



def graph(brute_force, branch_and_bound, greedy, dynamic, polynomial, random, ant, personal, tests):

    print("\n brute_force :     ", brute_force, "\n branch_and_bound :", branch_and_bound, "\n greedy :          ", greedy, "\n dynamic :         ", dynamic, "\n polynomial :      ", polynomial, "\n random :          ", random, "\n ant_colony :      ", ant, "\n personal :        ", personal, "\n\n test files :      ", tests, flush=True)
    print()


    
    if len(brute_force) != 0 :
        plt.plot(tests, brute_force, label='Brute force', marker = '.', color = 'royalblue')
    
    if len(branch_and_bound) != 0 :
        plt.plot(tests, branch_and_bound, label='Banch and bound', marker = '.', color = 'orange')
    
    if len(greedy) != 0 :
        plt.plot(tests, greedy, label = 'Greedy', marker = '.', color = 'limegreen')
    
    if len(dynamic) != 0 :
        plt.plot(tests, dynamic, label = 'Dynamic', marker = '.', color = 'r')
    
    if len(polynomial) != 0 :
        plt.plot(tests, polynomial, label = 'Polynomial', marker = '.', color = 'm')
    
    if len(random) != 0 :
        plt.plot(tests, random, label = 'Random', marker = '.', color = 'c')
    
    if len(ant) != 0 :
        plt.plot(tests, ant, label = 'Ant colony', marker = '.', color = 'hotpink')

    if len(personal) != 0 :
        plt.plot(tests, personal, label = '\'Personal\'', marker = '.', color = 'y')

    plt.grid()
    plt.ylabel('Time')
    plt.xlabel('Test file')

    plt.title("Graph title", fontname = "Times New Roman", fontsize = 15, fontweight = "bold", y = 1.02)

    plt.legend()
    plt.show()

    
