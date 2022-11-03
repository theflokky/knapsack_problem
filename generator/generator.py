import sys
import random
param = {'nbitems' : 0,
              'capacity' : 0,
              'minvalue' : 0,
              'maxvalue' : 0,
              'minweight' : 0,
              'maxweight' : 0}

def take_input(n):
        for idx, key in enumerate(param):
            if idx > n - 1:
                param[key] = abs(int(input(f'{key} :\n>>>')))

def generate_file() -> str:
    output = f'{param["nbitems"]} {param["capacity"]}\n'
    for i in range(param['nbitems']):
        output = output + f'{random.randint(param["minvalue"], param["maxvalue"])} {random.randint(param["minweight"], param["maxweight"])}\n'
    return output


if __name__ == "__main__":
    try :
        del sys.argv[0]
        for idx, key in enumerate(param):
            if idx < len(sys.argv):
                param[key] = int(sys.argv[idx])
                
        take_input(len(sys.argv))
    except Exception as e:
        print(e)
        print("*"*30)
        print("Usage : python3.10 generator.py [parameters] [files]")
        print("\tParameters being ints assigned to (in order) nbitems, capacity, minvalue, maxvalue, minweight, maxweight.")
        print("\tIt isn't mandatory to fill every parameter, the missing ones will be asked as inputs.")
        print("\tIf all 6 parameters are given, the extra arguments are filenames in which knapsack problems will be generated.\nIf no file is given, one will be asked.")
        print("In the next exemple, only nbitems, capacity and minvalue are assigned :")
        print("> py generator.py 5 20 4\nmaxvalue :\n>>>12\nminweight :\n>>>4\nmaxweight :\n>>>8")
        print("*"*30)
        sys.exit()
    print(param)
    if len(sys.argv) >6:
        for element in sys.argv[6:]:
            with open(element, "w") as target:
                target.write(generate_file())
    else :
        with open(input("Target file :\n>>>"), "w") as target:
                target.write(generate_file())
        

        
        