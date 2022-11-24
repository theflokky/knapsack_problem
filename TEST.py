

file = "/home/tyrannide/Fac/M1/Algo/knapsack_problem/test_files/All-MKP-Instances/gk/gk01.dat"
acc = 0
nmbo = 0

with open(file, "r") as f :
    data = f.read()

    ligne = data.split("\n")
ligne = ligne[1:-3]

liste_objects = []
obj = []

for l in ligne: 
    for mot in l.split():
        obj.append(mot)
        acc += 1
        if acc == 16:
            print(f"1 Objet et son profit\n\t{obj}, {len(obj)}\n")
            acc = 0
            nmbo += 1
            liste_objects.append(obj)
            obj = []

print(nmbo, liste_objects, len(liste_objects))