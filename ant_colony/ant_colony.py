import os.path
import random
import math

# instances_01_KP/large_scale/knapPI_1_100_1000_1

MINPHERO = 0.01
MAXPHERO = 6
RHO = 0.90
ALPHA = 1
BETA = 5


def printObejects(objects):
    for i in objects.items() :
        print(i)
    print("\n")

def defCandi(candidates) :
    for i in objects.items():
        candidates.update({i[0] : 1})

def defPhero(phero) : 
    for j in objects.items():
        tmp = []
        tmp.append(0)
        for i in objects.items():
            if j[0] == i[0]:
                tmp.append(0)
            else :
                tmp.append(MAXPHERO)    
        phero.update({j[0] : tmp})
    tmp[len(tmp)-1]=MAXPHERO
    phero.update({0 : tmp})
    

def sumPheroValue(phero,objects,candidates,actu) :
    sum=0
    for i in objects.items() :
        if candidates[i[0]] == 1 :
            sum += math.pow(phero[actu][i[0]],ALPHA)*math.pow((objects[i[0]][0]/objects[i[0]][1]),BETA)
    return sum

def updatePhero(phero): 
    for i in phero.items() :
        tmp = []
        
        if phero[i[0]][0]*RHO < MINPHERO :
            tmp.append(MINPHERO)
        else :
            tmp.append(phero[i[0]][0]*RHO)
        for j in phero.items():
            if i[0] == j[0] :
                tmp.append(0)
            elif phero[i[0]][j[0]]*RHO < MINPHERO :
                tmp.append(MINPHERO)
            else :
                tmp.append(phero[i[0]][j[0]]*RHO)
        phero.update({i[0] : tmp})


def setPhero(phero,bestSolution,result):
    p = 1/(1+bestSolution['value']-result['value'])
    prec = 0
    for i in result["number"] :
        if phero[i][prec]+p > MAXPHERO :
            phero[i][prec] = MAXPHERO
            phero[prec][i] = MAXPHERO
        else :
            phero[i][prec] = phero[i][prec]+p
            phero[prec][i] = phero[prec][i]+p
        prec = i

def setProb(probabilites, phero ,objects,candidates,actu):
    p = sumPheroValue(phero,objects,candidates,actu)
    maxProb = 0
    for i in candidates.items():
        if i[1] == 1 :
            minProb = maxProb
            maxProb += (math.pow(phero[actu][i[0]],ALPHA)*math.pow((objects[i[0]][0]/objects[i[0]][1]),BETA))/p
            probabilites.update({i[0] : [minProb, maxProb]})
        else :
            probabilites.update({i[0] : [-1, -1]}) # modif

while True:
    try :
        # Get file name and check if exist --------------------
        print("\nTo quit : CTRL-C")
        name = input("File name : ")
        
        # Load file data ----------------------------------
        with open(name, "r") as f :
            allFile = f.read()
            line = allFile.split("\n")
            
        # Split file data ---------------------------------
        line = line[:-2] # Don't take last line (the solution)
        nb, w = line[0].split()
        n = int(nb)   # Number of items
        wmax = int(w) # Max Weight 
        line = line[1:] # Don't take first line (n, wmax)

        objects = {}
        allValue = 0
        allW = 0
        i = 0
        for l in line :
            # Put all objects in 'objects'
            value, w = l.split()
            i+=1
            objects.update({i : [int(value),int(w)]})
            allValue = allValue + int(value)
            allW = allW + int(w)
          

        phero = {}
        defPhero(phero)

        # Create the probabilities table 
        probabilities = {}

        bestSolution ={'number' :[], 'value' : -1 , 'weight': -1}

        nbAnts = input("How many ants : ")

        
        for ant in range(int(nbAnts)) :

            result = {'number' :[], 'value' : 0 , 'weight': 0}
            allValueTmp = allValue
            
            # Create candidates list
            candidates = {}
            defCandi(candidates)

            cantGo = 0
            actu = 0
            #First item
            x = random.random()
            setProb(probabilities,phero,objects,candidates,actu)
            for j in probabilities.items():
                if x >= j[1][0] and x < j[1][1] and (result["weight"]+objects[j[0]][1]) <= wmax:
                    candidates.update({j[0] : 0})
                    cantGo += 1
                    actu = j[0]
                    result["number"].append(j[0])
                    result["value"] += objects[j[0]][0]
                    result["weight"] += objects[j[0]][1]
                    break
                elif (result["weight"]+objects[j[0]][1]) > wmax :
                    candidates.update({j[0] : 0})
                    cantGo += 1

            while cantGo<=n:
                x = random.random()
                setProb(probabilities,phero,objects,candidates,actu)
                for j in probabilities.items():
                    if x >= j[1][0] and x < j[1][1] and (result["weight"]+objects[j[0]][1]) <= wmax:
                        candidates.update({j[0] : 0})
                        cantGo += 1
                        actu = j[0]
                        result["number"].append(j[0])
                        result["value"] += objects[j[0]][0]
                        result["weight"] += objects[j[0]][1]
                        break
                    elif (result["weight"]+objects[j[0]][1]) > wmax :
                        candidates.update({j[0] : 0})
                        cantGo += 1
                    
            if result["value"] > bestSolution["value"] :
                bestSolution = result
            
            #printObejects(phero)
            updatePhero(phero)
            #printObejects(phero)
            setPhero(phero,bestSolution,result)
            

        sorted = bestSolution["number"]
        sorted.sort()
        print(sorted)
        print(f"{bestSolution['value']}\nweith : {bestSolution['weight']}/{wmax}\n")
                

    except KeyboardInterrupt:
        """ To stop the program ! """
        print("\nBye !")
        break
    except FileNotFoundError:
        """ If file not exist ! """
        print("The file doesn't exist !\nBye !\n")
        break
