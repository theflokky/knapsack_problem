import time

# DATA
items = ['map', 'compass', 'water', 'sandwich', 'glucose', 'tin', 'banana',\
'apple', 'cheese', 'beer', 'suntan', 'camera', 'T', 'trousers', 'umbrella', 'w t', 'w o', \
'note-case', 'sunglasses', 'towel', 'socks', 'book']
weights = [9, 13, 153, 50, 15, 68, 27, 39, 23, 52, 11, 32, 24, 48, 73, 42, 43, 22, 7, 18, 4, 30]
values = [150, 35, 200, 160, 60, 45, 60, 40, 30, 10, 70, 30, 15, 10, 40, 70, 75, 80, 20, 12, 50, 10]

a = sorted(zip(items, weights, values), key= lambda x : -x[2]/x[1])
items = [i for i,_,_ in a]
weights = [i for _,i,_ in a]
values = [i for _,_,i in a]



N_ITEMS = min(len(items), len(weights), len(values)) #number of items


print("Nombre d'items", N_ITEMS)


sum = 0
j = 0
for j in range(N_ITEMS) :
    sum = sum+weights[j]

print("weight :", sum)


sum = 0
j = 0
for j in range(N_ITEMS) :
    sum = sum+values[j]

print("value :", sum)




M = 400 #size of the knacksack


finalWeight = 0
finalValue = 0
X = []
Y = []

def banchBound() :
    currentValue = 0
    currentWeight = 0
    i = 0 #index of item
    banchBoundRec(currentValue, currentWeight, 0)





def banchBoundRec(currentValue, currentWeight, i) :
    global values, weights, M, finalWeight, finalValue, X, Y


    if(currentWeight + weights[i] <= M):
        Y[i] = 1

        if(i < N_ITEMS-1):
            banchBoundRec(currentValue + values[i], currentWeight + weights[i], i+1)

        if((currentValue + values[i] > finalValue) and (i == N_ITEMS-1)) :
            finalValue = currentValue + values[i]
            finalWeight = currentWeight + weights[i]
            X = []
            for j in Y :
                X.append(j)

            
            
    if (bound(currentValue, currentWeight, i) >= finalValue) :
        Y[i] = 0

        if(i < N_ITEMS-1) :
            banchBoundRec(currentValue, currentWeight, i+1)

        if((currentValue > finalValue) and (i == N_ITEMS-1)) :
            finalValue = currentValue
            finalWeight = currentWeight
            X = []
            for j in Y :
                X.append(j)





def bound(currentValue, currentWeight, i) :
    global values, weights, M, finalWeight, finalValue, X, Y
    v = currentValue
    w = currentWeight
    for j in range(i+1, N_ITEMS) :
        if (w + weights[j] <= M):
            w = w + weights[j]
            v = v + values[j]
    return v







while len(Y) < N_ITEMS:
    Y.append(0)


print()

start = time.time()
banchBound()
end = time.time()

print ("Final Weight: ", finalWeight)
print ("Final Value: ", finalValue)
print ("Items: ", X)

Z=[]
j = 0
for j in range(N_ITEMS) :
    if(X[j]):
        Z.append(items[j])

print("Item Names :", Z)

print()
print("time : ", (end-start))
print("------------- END -----------")