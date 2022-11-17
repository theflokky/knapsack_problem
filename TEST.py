

file = "/home/tyrannide/Fac/M1/Algo/knapsack_problem/All-MKP-Instances/gk/gk01.dat"
acc = 0
nmbo = 0

with open(file, "r") as f :
    data = f.read()

    ligne = data.split("\n")
ligne = ligne[1:-3]

for l in ligne: 
    for mot in l.split():
        acc += 1
        if acc == 16:
            print("1 Objet et son profit\n")
            acc = 0
            nmbo += 1

print(nmbo)