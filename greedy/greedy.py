import time

# The size of a runnable sublist
MINIMUM = 32

# Returns the minimum length of a runnable sublist
# From 23 - 64
# Such that len(list)/minrun is less or equal
# To a power of 2

def find_minrun(n):
    r = 0
    while n >= MINIMUM: 
        r |= n & 1
        n >>= 1
    return n + r 

# Sorting runnable size of list
# From left to right
def insertion_sort(list, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and list[j][0]/list[j][1] > list[j - 1][0]/list[j - 1][1]:
            list[j], list[j-1] = list[j - 1], list[j]
            j -= 1

# Merging function to unify all sublist
def merge(list, l, m, r):
    # breaking up in two parts the list:
    # The first half
    len1 = m - l + 1
    # The second half
    len2 = r - m

    left, right = [], []

    # Creating left part
    for i in range(0, len1):
        left.append(list[l+i])

    # Creating right part
    for i in range(0, len2):
        right.append(list[m + 1 + i])

    i, j, k = 0, 0, l

    # After comparing the list, we merge them
    while i < len1 and j < len2:
        if left[i][0]/left[i][1] < right[j][0]/right[j][1]:
            list[k] = right[j]
            j+=1
        else:
            list[k] = left[i]
            i+=1
        k+=1

    # The comparison has ended, we check if any list is non-empty
    # If so we fill our list with the leftover

    # copy if needed remnants from left
    while(i < len1):
        list[k] = left[i]
        k+=1
        i+=1

    #copy if needed remnants from right
    while(j < len2):
        list[k] = right[j]
        k+=1
        j+=1

# Main function for timsort
# Returns the sorted list
def timsort(list):
    n = len(list)
    minrun = find_minrun(n)

    # Called for sorting runnable list sizes
    for start in range(0, n, minrun):
        end = min(start + minrun-1, n-1)
        insertion_sort(list, start, end)

    # Merging multiple sublist together
    size = minrun
    while size < n:

        for left in range(0, n, 2*size):
            mid = min(n - 1, left + size - 1)
            right = min( (left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(list, left, mid, right)

        size = 2 * size

def greedy(lo, w) :

    start_process = time.time()

    #Short life time list to prevent losing info
    lot = lo
    #Current availabilty of the knapsack
    cw = w

    #Current list of object inside the knapsack
    loiks = []

    #Final value of the knapsack
    fv = 0


    # New version implementing the timsort
    timsort(lot)

    for i in range (0,len(lot)):
        if(cw - int(lot[i][1]) > 0):
            cw -= int(lot[i][1])
            fv += int(lot[i][0])
            loiks.append(lot[i])
        else :
            break

    end_process = time.time()

    return (end_process - start_process), loiks, fv