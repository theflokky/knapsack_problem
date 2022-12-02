
import graph

#Les temps pour chaque algo
brute_force =       [0.01, 0.60, 2.40, 5.00]
branch_and_bound =  [0.09, 0.12, 0.50, 0.80]
greedy =            [0.05, 0.09, 0.40, 1.20]
dynamic =           [0.10, 0.90, 1.80, 3.00]
polynomial =        [1.00, 2.00, 3.00, 4.00]
random =            [2.00, 2.50, 3.20, 4.60]
ant =               [0.70, 1.80, 3.50, 4.50]
personal =          [1.50, 1.50, 1.50, 1.50]

#La liste des fichiers testés (! dans l'ordre)
tests = ["file_1", "file_2", "file_3", "file_4"]

graph.graph(brute_force, branch_and_bound, greedy, dynamic, polynomial, random, ant, personal, tests)