# test program for the graph creation program

import graph

# time for each algorithm
time = {
"brute_force" :         [0.01, 0.60, 2.40, 5.00],
"branch_and_bound" :    [0.09, 0.12, 0.50, 0.80],
"greedy" :              [2.00, 2.50, 3.20, 4.60],
"greedy_value" :        [2.50, 3.00, 3.70, 5.10],
"greedy_weight" :       [3.00, 3.50, 4.20, 5.60],
"dynamic_programming" : [0.10, 0.90, 1.80, 3.00],
"polynomial" :          [1.00, 2.00, 3.00, 4.00],
"grasp" :               [0.05, 0.09, 0.40, 1.20],
"ant_colony" :          [0.70, 1.80, 3.50, 4.50],
"personal" :            [1.50, 1.50, 1.50, 1.50]
}

# list of file names
tests = ["file_1", "file_2", "file_3", "file_4"]

# graph creation
graph.graph(time, tests)
