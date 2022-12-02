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





class Tree:

    def __init__(self, left = None, right = None, finalItems = [], currentValue = 0, currentWeight = 0):
        self.left = left
        self.right = right
        self.items = finalItems
        self.value = currentValue
        self.weight = currentWeight

    def setLeft(self, left):
        self.left = left

    def setRight(self,right):
        self.right = right

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right


    def __repr__(self, level=0):
        ret = "    "*level+repr(self.items)+"\n"
        if(self.left != None):
            ret+=self.left.__repr__(level+1)
        if(self.right != None):
            ret+=self.right.__repr__(level+1)
        return ret

    def printLeaves(self):
        if(self.left == None and self.right == None):
            print(self.items)
        else:
            if(self.right != None):
                self.left.printLeaves()
            if(self.right != None):
                self.right.printLeaves()




X=[]
currentValue = 0
currentWeight = 0
A = Tree(None, None, X.copy(), currentValue, currentWeight)
X.append(items[1])
currentValue += values[1]
currentWeight += weights[1]
B = Tree(None, None, X.copy(), currentValue, currentWeight)
X.append(items[2])
currentValue += values[2]
currentWeight += weights[2]
C = Tree(None, None, X.copy(), currentValue, currentWeight)
X.remove(items[2])
X.append(items[3])
currentValue += -values[2] + values[3]
currentWeight += -weights[2] + weights[3]
D = Tree(None, None, X.copy(), currentValue, currentWeight)

X=[]
currentValue = 0
currentWeight = 0
X.append(items[4])
currentValue += values[4]
currentWeight += weights[4]
E = Tree(None, None, X.copy(), currentValue, currentWeight)
X.append(items[5])
currentValue += values[5]
currentWeight += weights[5]
F = Tree(None, None, X.copy(), currentValue, currentWeight)
X.remove(items[5])
X.append(items[6])
currentValue += -values[5] + values[6]
currentWeight += -weights[5] + weights[6]
G = Tree(None, None, X.copy(), currentValue, currentWeight)





B.setLeft(C)
B.setRight(D)
A.setLeft(B)
E.setLeft(F)
E.setRight(G)
A.setRight(E)

print(A)
print()


def createTree():
    T = Tree()
    return createTreeRec(T)



def createTreeRec(T, i=0):
    s = T.items.copy()
    s.append(items[i])
    L = Tree(None, None, s, T.value+values[i], T.weight+weights[i])
    R = Tree(None, None, T.items.copy(), T.value, T.weight)

    i += 1
    
    if(i < 20):
        createTreeRec(L, i)
        createTreeRec(R, i)

    T.setLeft(L)
    T.setRight(R)
    
    return T





def banchBound() :
    currentValue = 0
    currentWeight = 0
    i = 0 #index of item
    banchBoundRec(currentValue, currentWeight, 0)



def banchBoundRec(currentValue, currentWeight, i) :
    return 0



















while len(Y) < N_ITEMS:
    Y.append(0)


print()

start = time.time()

createTree()

banchBound()
end = time.time()



print ("Final Weight: ", finalWeight)
print ("Final Value: ", finalValue)
print ("Items: ", X)

Z=[]
j = 0
#for j in range(N_ITEMS) :
#    if(X[j]):
#SS        Z.append(items[j])

print("Item Names :", Z)

print()
print("time : ", (end-start))
print("------------- END -----------")