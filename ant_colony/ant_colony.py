import os.path
import random
import math

# instances_01_KP/large_scale/knapPI_1_100_1000_1

MINPHERO = 0.01
MAXPHERO = 6
RHO = 0.99
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
    for i in objects.items():
        phero.update({i[0] : MAXPHERO})

def sumPheroValue(phero,objects,candidates) :
    sum=0
    for i in phero.items() :
        if candidates[i[0]] == 1 :
            sum += math.pow(i[1],ALPHA)*math.pow(objects[i[0]][0],BETA)
    return sum

def updatePhero(phero):
    for i in phero.items() :
        if phero[i[0]]*RHO < MINPHERO :
            phero.update({i[0] : MINPHERO})
        else :
            phero.update({i[0] : phero[i[0]]*RHO})

def setPhero(phero,bestSolution,result):
    p = 1/(1+bestSolution['value']-result['value'])
    for i in result["number"] :
        if phero[i]+p > MAXPHERO :
            phero.update({i : MAXPHERO})
        else :
            phero.update({i : phero[i]+p})

def setProb(probabilites, phero ,objects,candidates):
    j = sumPheroValue(phero,objects,candidates)
    maxProb = 0
    for i in candidates.items():
        if i[1] == 1 :
            minProb = maxProb
            maxProb += (math.pow(phero[i[0]],ALPHA)*math.pow(objects[i[0]][0],BETA))/j
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
            while cantGo<=n:
                x = random.random()
                setProb(probabilities,phero,objects,candidates)
                for j in probabilities.items():
                    if x >= j[1][0] and x < j[1][1] and (result["weight"]+objects[j[0]][1]) <= wmax:
                        candidates.update({j[0] : 0})
                        cantGo += 1
                        result["number"].append(j[0])
                        result["value"] += objects[j[0]][0]
                        result["weight"] += objects[j[0]][1]
                        break
                    elif (result["weight"]+objects[j[0]][1]) > wmax :
                        candidates.update({j[0] : 0})
                        cantGo += 1
                    
            if result["value"] > bestSolution["value"] :
                bestSolution = result
            
            updatePhero(phero)
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
