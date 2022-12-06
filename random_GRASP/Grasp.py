import random
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
def insertion_sort_01(list, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left :
            if list[j-1][1] != 0 and list[j][1]!=0 :
                if list[j][0]/list[j][1] <= list[j - 1][0]/list[j - 1][1] :
                    break
            elif list[j-1][1] == 0 and list[j][1]!=0 :
                if list[j][0]/list[j][1] <= list[j - 1][0] :
                    break
            elif list[j-1][1] != 0 and list[j][1]==0 :
                if list[j][0] <= list[j - 1][0]/list[j - 1][1] :
                    break
            elif list[j-1][1] == 0 and list[j][1]==0 :
                if list[j][0] <= list[j - 1][0] :
                    break
                
            list[j], list[j-1] = list[j - 1], list[j]
            j -= 1

# Merging function to unify all sublist
def merge_01(list, l, m, r):
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
def timsort_01(list):
    n = len(list)
    minrun = find_minrun(n)

    # Called for sorting runnable list sizes
    for start in range(0, n, minrun):
        end = min(start + minrun-1, n-1)
        insertion_sort_01(list, start, end)

    # Merging multiple sublist together
    size = minrun
    while size < n:

        for left in range(0, n, 2*size):
            mid = min(n - 1, left + size - 1)
            right = min( (left + 2 * size - 1), (n - 1))

            if mid < right:
                merge_01(list, left, mid, right)

        size = 2 * size




def greedy_randomised_construction(lo, kc):

    lt = lo[:]
    cw = kc
    final_list = []
    final_value = 0

    timsort_01(lt)

    while len(lt) > 0:
        current_candidates = []
        for i in range(3):
            if i < len(lt):
                current_candidates.append(lt[i])

        
        chosen_object = random.choice(current_candidates)
        if chosen_object[1] <= cw:
            final_list.append(chosen_object)
            cw -= chosen_object[1]
            final_value += chosen_object[0]

        lt.pop(lt.index(chosen_object))

    

    

    return final_list, final_value





def grasp_main(lo, nbI, w):
    best = 0
    l = []
    solution = []
    v = 0
    for i in range(nbI):

        l, v = greedy_randomised_construction(lo, w)


        if v > best:
            best = v
            solution = l[:]

    return solution, best

def grasp(lo, nbI, w):
    start_process = time.time()

    loiks, fv = grasp_main(lo, nbI, w)

    end_process = time.time()

    return (end_process - start_process), loiks, fv



# Multi-dimensional version :



# Sorting runnable size of list
# From left to right
def insertion_sort_multi(list, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and list[j][0]/(sum(list[j][1])/len(list[j][1])) > list[j - 1][0]/(sum(list[j - 1][1])/len(list[j][1])):
            list[j], list[j-1] = list[j - 1], list[j]
            j -= 1



# Merging function to unify all sublist
def merge_multi(list, l, m, r):
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
        if left[i][0]/sum(left[i][1])/len(left[i][1]) < right[j][0]/sum(right[j][1])/len(right[j][1]):
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




# Main function just like 0/1 version
def timsort_multi(l):
    n = len(l)
    minrun = find_minrun(n)

    # Called for sorting runnable list sizes
    for start in range(0, n, minrun):
        end = min(start + minrun-1, n-1)
        insertion_sort_multi(l, start, end)

    # Merging multiple sublist together
    size = minrun
    while size < n:

        for left in range(0, n, 2*size):
            mid = min(n - 1, left + size - 1)
            right = min( (left + 2 * size - 1), (n - 1))

            if mid < right:
                merge_multi(l, left, mid, right)

        size = 2 * size


def greedy_randomised_construction_multi(lo, kc):

    lt = lo[:]
    cw = kc[:]
    final_list = []
    final_value = 0

    timsort_multi(lt)

    while len(lt) > 0:
        current_candidates = []
        for i in range(3):
            if i < len(lt):
                current_candidates.append(lt[i])

        
        chosen_object = random.choice(current_candidates)
        for i in range(0, len(chosen_object[1])):
            if chosen_object[1][i] > cw[i]:
                break
        else :
            final_list.append(chosen_object)
            cw = [initial - object_weigth for initial, object_weigth in zip(cw, chosen_object[1])]
            final_value += chosen_object[0]


        lt.pop(lt.index(chosen_object))


    #verif_totaux_init = [0] * len(cw)
    #verif_totaux_sac = [0] * len(cw)
    #acc = 0
    #for i in lo:
    #    for j in i[1]:
    #        verif_totaux_init[acc] += j
    #        acc+= 1
    #    acc = 0
#
    #acc = 0
    #for i in final_list:
    #    for j in i[1]:
    #        verif_totaux_sac[acc] += j
    #        acc += 1
    #    acc = 0
#
    #print(verif_totaux_init,"\n",verif_totaux_sac,"\n", kc)
#
    #acc = 0
    #for i in kc:
    #    print(f"{i} {i - verif_totaux_sac[acc]} {verif_totaux_sac[acc]}")
    #    acc+=1

    return final_list, final_value

def grasp_multi_main(lo, nbI, w):
    best = 0
    l = []
    solution = []
    v = 0
    for i in range(nbI):

        l, v = greedy_randomised_construction_multi(lo, w)


        if v > best:
            best = v
            solution = l[:]

    return solution, best


def grasp_multi(lo, nbI, w):

    start_process = time.time()

    loiks, fv = grasp_multi_main(lo, nbI, w)

    end_process = time.time()

    return (end_process - start_process), loiks, fv
