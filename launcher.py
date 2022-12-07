# apt-get install python3-tk

import tkinter as tk
import os
import greedy.greedy_value as greedyV
import greedy.greedy_weight as greedyW
import greedy.greedy as greedy
import ant_colony.ant_colony as ant
import brute_force.brute_force as bruteForce
import branch_and_bound.branch_and_bound as branch
import random_GRASP.Grasp as grasp
import dynamic_programming.dynamic_programming as dyna
import fptas.fptas as fptas
import personal_approach.meet_in_the_middle as perso
import graph 

class ChecklistBox(tk.Frame):
    def __init__(self, parent, choices, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)

        self.vars = []
        bg = self.cget("background")
        for choice in choices:
            var = tk.StringVar(value=choice)
            self.vars.append(var)
            cb = tk.Checkbutton(self, var=var, text=choice,
                                onvalue=choice, offvalue="",
                                anchor="w", width=20, background=bg,
                                relief="flat", highlightthickness=0
            )
            cb.pack(side="top", fill="x", anchor="w")
        

    def getCheckedItems(self):
        values = []
        for var in self.vars:
            value =  var.get()
            if value:
                values.append(value)
        return values

class App() :
    def __init__(self,parent) :
        self.parent = parent
        self.entry = tk.Entry(self.parent)

        self.comp = {"ant_colony":[],"branch_and_bound":[],"brute_force":[],"dynamic_programming":[],"greedy_value":[],"greedy_weight":[],"greedy":[],"grasp":[],"polynomial":[],"personal":[]}
        self.compF = []    

        self.parent.title("knapsack")
        self.parent.geometry("1200x800")

        self.knapsnack_problem = ["0/1","multidimensional"]
        self.type_file = ["low-dimensional","large_scale","personal_files"]
        self.files = [f for f in os.listdir("test_files/low-dimensional")]
        self.algos = ["ant_colony","branch_and_bound","brute_force","dynamic_programming","greedy_value","greedy_weight","greedy","grasp","polynomial","personal","comp"]

        self.algos01 = ["ant_colony","branch_and_bound","brute_force","dynamic_programming","greedy_value","greedy_weight","greedy","grasp","polynomial","personal","comp"]
        self.algos_muti = ["brute_force","greedy_value","greedy_weight","greedy","grasp","comp"]

        self.chubeas = [f for f in os.listdir("test_files/All-MKP-Instances/chubeas/OR10x100")]
        self.choices = []

        # Option problem
        self.list_knapsnack_problem = tk.StringVar(self.parent)
        self.list_knapsnack_problem.set(self.knapsnack_problem[0])
        self.list_knapsnack_problem.trace('w',self.set_problem)

        self.label_knapsnack = tk.Label(self.parent, text="Problem : ")
        self.label_knapsnack.grid(column=175,row=0)
        
        self.all_knapsnack_problem = tk.OptionMenu(self.parent,self.list_knapsnack_problem, *self.knapsnack_problem)
        self.all_knapsnack_problem.grid(column=175,row=1)

        # Option types 
        self.list_type_file = tk.StringVar(self.parent)
        self.list_type_file.set(self.type_file[0])
        self.list_type_file.trace('w',self.set_files)

        self.label_file = tk.Label(self.parent, text="Which scale do you wish to work on ? ")
        self.label_file.grid(column=175,row=2)

        self.all_type_file = tk.OptionMenu(self.parent,self.list_type_file, *self.type_file)
        self.all_type_file.grid(column=175,row=3)

        # Option files
        self.list_files = tk.StringVar(self.parent)
        self.list_files.set(self.files[0])
        self.list_files.trace('w',self.set_chubeas)
    
        self.label_files = tk.Label(self.parent, text="Which file do you wish to work on ? ")
        self.label_files.grid(column=175,row=4)

        self.all_files = tk.OptionMenu(self.parent,self.list_files, *self.files)
        self.all_files.grid(column=175,row=5)

        self.label_ant = tk.Label(self.parent, text="How many interations ? (default = 30) ")
        self.nb_iter = tk.Entry(self.parent)

        # Option algos
        self.list_algos = tk.StringVar(self.parent)
        self.list_algos.trace('w',self.set_algo)
    
        self.label_files = tk.Label(self.parent, text="Which algorithm do you wish to launch ? ")
        self.label_files.grid(column=175,row=6)

        self.all_algos = tk.OptionMenu(self.parent,self.list_algos, *self.algos)
        self.all_algos.grid(column=175,row=7)

        # Launch button
        self.button = tk.Button(self.parent, text="Launch", command=self.launch)
        self.button.grid(column=175,row=10)

        self.choices = self.algos[:-1]
        self.checklist = ChecklistBox(self.parent, self.choices, bd=1, relief="sunken", background="white")

        # Chubeas
        self.list_chubeas = tk.StringVar(self.parent)
        self.list_chubeas.set(self.chubeas[0])
        self.all_chubeas = tk.OptionMenu(self.parent,self.list_chubeas,*self.chubeas)

        # Result
        self.time = tk.Label(self.parent,text="")
        self.obj = tk.Label(self.parent,text="")
        self.value = tk.Label(self.parent,text="")


    def set_problem(self,*args):
        pb = self.list_knapsnack_problem.get()
        al = self.list_algos.get()
        self.clear()
        for child in self.parent.winfo_children() :
            child.destroy()
        match pb :
            case "0/1" :
                self.type_file.clear()
                self.type_file.append("low-dimensional")
                self.type_file.append("large_scale")
                self.type_file.append("personal_files")
                self.files = [f for f in os.listdir("test_files/low-dimensional")]
                self.algos = self.algos01
            case "multidimensional" :
                self.type_file.clear()
                self.type_file.append("chubeas")
                self.type_file.append("gk")
                self.files = [f for f in os.listdir("test_files/All-MKP-Instances/chubeas")]
                self.chubeas = [f for f in os.listdir("test_files/All-MKP-Instances/chubeas/OR10x100")]

                self.list_chubeas = tk.StringVar(self.parent)
                self.list_chubeas.set(self.chubeas[0]) 
                self.all_chubeas = tk.OptionMenu(self.parent,self.list_chubeas,*self.chubeas)
                self.all_chubeas.grid(column=176,row=5)

                self.algos = self.algos_muti
                if al in self.algos_muti:
                    self.list_algos.set(al)
                else :
                    self.list_algos.set(self.algos[0])

        
        self.label_knapsnack = tk.Label(self.parent, text="Problem : ")
        self.label_knapsnack.grid(column=175,row=0)
        self.all_knapsnack_problem = tk.OptionMenu(self.parent,self.list_knapsnack_problem, *self.knapsnack_problem)
        self.all_knapsnack_problem.grid(column=175,row=1)

        self.label_file = tk.Label(self.parent, text="Which scale do you wish to work on ? ")
        self.label_file.grid(column=175,row=2)
        self.list_type_file.set(self.type_file[0])
        self.all_type_file = tk.OptionMenu(self.parent,self.list_type_file, *self.type_file)
        self.all_type_file.grid(column=175,row=3)
        
        self.label_files = tk.Label(self.parent, text="Which file do you wish to work on ? ")
        self.label_files.grid(column=175,row=4)
        self.list_files.set(self.files[0])
        self.all_files = tk.OptionMenu(self.parent,self.list_files, *self.files)
        self.all_files.grid(column=175,row=5)

        self.label_files = tk.Label(self.parent, text="Which algorithm do you wish to launch ? ")
        self.label_files.grid(column=175,row=6)

        self.all_algos = tk.OptionMenu(self.parent,self.list_algos, *self.algos)
        self.all_algos.grid(column=175,row=7)

        self.button = tk.Button(self.parent, text="Launch", command=self.launch)
        self.button.grid(column=175,row=10)

        self.label_ant = tk.Label(self.parent, text="How many iterations ? (default = 30) ")
        self.nb_iter = tk.Entry(self.parent)

        self.time = tk.Label(self.parent,text="")
        self.obj = tk.Label(self.parent,text="")
        self.value = tk.Label(self.parent,text="")


        if al == "ant_colony" or al == "grasp":
            self.label_ant.grid(column=175,row=8)
            self.nb_iter.grid(column=175,row=9)
        
        if al == "comp" :
            self.choices = self.algos[:-1]
            self.checklist = ChecklistBox(self.parent, self.choices, bd=1, relief="sunken", background="white")
            self.checklist.grid(column=175,row=8)

            self.clearB = tk.Button(self.parent, text="Clear comp", command=self.clear)
            self.clearB.grid(column=175,row=11)

            self.showB = tk.Button(self.parent, text="Show graph", command=self.show)
            self.showB.grid(column=176,row=11)


    def set_files(self,*args):
        ls = self.list_type_file.get()
        al = self.list_algos.get()
        self.clear()
        for child in self.parent.winfo_children() :
            child.destroy()
        match ls :
            case "low-dimensional":
                self.files = [f for f in os.listdir("test_files/low-dimensional")]
            case "large_scale":
                self.files = [f for f in os.listdir("test_files/large_scale")]
            case "personal_files":
                self.files = [f for f in os.listdir("test_files/personal_files")]

            case "chubeas" :
                self.files = [f for f in os.listdir("test_files/All-MKP-Instances/chubeas")]
                self.all_chubeas = tk.OptionMenu(self.parent,self.list_chubeas, *self.chubeas)
                self.all_chubeas.grid(column=176,row=5)
            case "gk" :
                self.files = [f for f in os.listdir("test_files/All-MKP-Instances/gk")]

        self.label_knapsnack = tk.Label(self.parent, text="Problem : ")
        self.label_knapsnack.grid(column=175,row=0)
        self.all_knapsnack_problem = tk.OptionMenu(self.parent,self.list_knapsnack_problem, *self.knapsnack_problem)
        self.all_knapsnack_problem.grid(column=175,row=1)

        self.label_file = tk.Label(self.parent, text="Which scale do you wish to work on ? ")
        self.label_file.grid(column=175,row=2)
        self.all_type_file = tk.OptionMenu(self.parent,self.list_type_file, *self.type_file)
        self.all_type_file.grid(column=175,row=3)
        
        self.label_files = tk.Label(self.parent, text="Which file do you wish to work on ? ")
        self.label_files.grid(column=175,row=4)
        self.list_files.set(self.files[0])
        self.all_files = tk.OptionMenu(self.parent,self.list_files, *self.files)
        self.all_files.grid(column=175,row=5)

        self.label_files = tk.Label(self.parent, text="Which algorithm do you wish to launch ? ")
        self.label_files.grid(column=175,row=6)

        self.all_algos = tk.OptionMenu(self.parent,self.list_algos, *self.algos)
        self.all_algos.grid(column=175,row=7)

        self.button = tk.Button(self.parent, text="Launch", command=self.launch)
        self.button.grid(column=175,row=10)

        self.label_ant = tk.Label(self.parent, text="How many iterations ? (default = 30) ")
        self.nb_iter = tk.Entry(self.parent)

        self.time = tk.Label(self.parent,text="")
        self.obj = tk.Label(self.parent,text="")
        self.value = tk.Label(self.parent,text="")

        if al == "ant_colony" or al == "grasp":
            self.label_ant.grid(column=175,row=8)
            self.nb_iter.grid(column=175,row=9)

        if al == "comp" :
            self.choices = self.algos[:-1]
            self.checklist = ChecklistBox(self.parent, self.choices, bd=1, relief="sunken", background="white")
            self.checklist.grid(column=175,row=8)

            self.clearB = tk.Button(self.parent, text="Clear comp", command=self.clear)
            self.clearB.grid(column=175,row=11)

            self.showB = tk.Button(self.parent, text="Show graph", command=self.show)
            self.showB.grid(column=176,row=11)

    def set_algo(self,*args):
        type = self.list_type_file.get()
        al = self.list_algos.get()
        ls = self.list_files.get()
        ch = self.list_chubeas.get()
        for child in self.parent.winfo_children() :
            child.destroy()

        self.label_knapsnack = tk.Label(self.parent, text="Problem : ")
        self.label_knapsnack.grid(column=175,row=0)
        self.all_knapsnack_problem = tk.OptionMenu(self.parent,self.list_knapsnack_problem, *self.knapsnack_problem)
        self.all_knapsnack_problem.grid(column=175,row=1)

        self.label_file = tk.Label(self.parent, text="Which scale do you wish to work on ? ")
        self.label_file.grid(column=175,row=2)
        self.all_type_file = tk.OptionMenu(self.parent,self.list_type_file, *self.type_file)
        self.all_type_file.grid(column=175,row=3)
        
        self.label_files = tk.Label(self.parent, text="Which file do you wish to work on ? ")
        self.label_files.grid(column=175,row=4)
        self.list_files.set(ls)
        self.all_files = tk.OptionMenu(self.parent,self.list_files, *self.files)
        self.all_files.grid(column=175,row=5)

        if type == "chubeas" :
            self.list_chubeas.set(ch)
            self.all_chubeas = tk.OptionMenu(self.parent,self.list_chubeas, *self.chubeas)
            self.all_chubeas.grid(column=176,row=5)

        self.label_files = tk.Label(self.parent, text="Which algorithm do you wish to launch ? ")
        self.label_files.grid(column=175,row=6)

        self.all_algos = tk.OptionMenu(self.parent,self.list_algos, *self.algos)
        self.all_algos.grid(column=175,row=7)

        self.button = tk.Button(self.parent, text="Launch", command=self.launch)
        self.button.grid(column=175,row=10)

        self.label_ant = tk.Label(self.parent, text="How many iterations ? (default = 30) ")
        self.nb_iter = tk.Entry(self.parent)

        self.time = tk.Label(self.parent,text="")
        self.obj = tk.Label(self.parent,text="")
        self.value = tk.Label(self.parent,text="")
        
        if al == "ant_colony" or al == "grasp":
            self.label_ant.grid(column=175,row=8)
            self.nb_iter.grid(column=175,row=9)
        
        if al == "comp" :
            self.checklist = ChecklistBox(root, self.choices, bd=1, relief="sunken", background="white")
            self.checklist.grid(column=175,row=8)

            self.clearB = tk.Button(self.parent, text="Clear comp", command=self.clear)
            self.clearB.grid(column=175,row=11)

            self.showB = tk.Button(self.parent, text="Show graph", command=self.show)
            self.showB.grid(column=176,row=11)

    def set_chubeas(self,*args):
        type = self.list_type_file.get()
        file = self.list_files.get()
        if type == "chubeas" :
            way = "test_files/All-MKP-Instances/chubeas/" + file
            self.chubeas = [f for f in os.listdir(way)]
            self.list_chubeas.set(self.chubeas[0])

    def launch(self,*args):
        pb = self.list_knapsnack_problem.get()
        al = self.list_algos.get()
        way = self.list_type_file.get()
        file = self.list_files.get()
        ch = self.list_chubeas.get()
        match pb :
            case "0/1" :
                n,wmax,list_objects = load(way,file)
                match al:
                    case "ant_colony" :
                        if str(self.nb_iter.get()).isnumeric() :
                            nb = int(self.nb_iter.get())
                        else :
                            nb = 30
                        t,obj,value = ant.ant(list_objects,nb,n,wmax)
                    case "branch_and_bound" :
                        t,obj,value = branch.banchBound(n, wmax, list_objects)
                    case "brute_force" :
                        t,obj,value = bruteForce.bruteForce(wmax,list_objects)
                    case "dynamic_programming" :
                        t,obj,value = dyna.dynamic(list_objects,wmax)
                    case "greedy_value" :
                        t,obj,value = greedyV.greedy_value_01(list_objects,wmax)
                    case "greedy_weight" :
                        t,obj,value = greedyW.greedy_weight_01(list_objects,wmax)
                    case "greedy" :
                        t,obj,value = greedy.greedy_01(list_objects,wmax)
                    case "polynomial" :
                        t,obj,value = fptas.fptas(1,wmax,list_objects)
                    case "grasp" :
                        if str(self.nb_iter.get()).isnumeric() :
                            nb = int(self.nb_iter.get())
                        else :
                            nb = 30
                        t,obj,value = grasp.grasp(list_objects, nb, wmax)
                    case "personal":
                        t,obj,value = perso.meet_in_the_middle(list_objects, wmax)
                    case "comp" :
                        tmp = self.checklist.getCheckedItems()
                        self.compF.append(file)
                        for a in tmp :
                            match a :
                                case "ant_colony" :
                                    nb = 30
                                    t,obj,value = ant.ant(list_objects,nb,n,wmax)
                                    self.comp["ant_colony"].append(t)
                                case "branch_and_bound" :
                                    t,obj,value = branch.banchBound(n, wmax, list_objects)
                                    self.comp["branch_and_bound"].append(t)
                                case "brute_force" :
                                    t,obj,value = bruteForce.bruteForce(wmax,list_objects)
                                    self.comp["brute_force"].append(t)
                                case "dynamic_programming" :
                                    t,obj,value = dyna.dynamic(list_objects,wmax)
                                    self.comp["dynamic_programming"].append(t)
                                case "greedy_value" :
                                    t,obj,value = greedyV.greedy_value_01(list_objects,wmax)
                                    self.comp["greedy_value"].append(t)
                                case "greedy_weight" :
                                    t,obj,value = greedyW.greedy_weight_01(list_objects,wmax)
                                    self.comp["greedy_weight"].append(t)
                                case "greedy" :
                                    t,obj,value = greedy.greedy_01(list_objects,wmax)
                                    self.comp["greedy"].append(t)
                                case "grasp" :
                                    nb = 30
                                    t,obj,value = grasp.grasp(list_objects, nb, wmax)
                                    self.comp["grasp"].append(t)
                                case "polynomial":
                                    t,obj,value = fptas.fptas(1,wmax,list_objects)
                                    self.comp["polynomial"].append(t)
                                case "personal":
                                    t,obj,value = perso.meet_in_the_middle(list_objects, wmax)
                                    self.comp["personal"].append(t)
                    case _ :
                        print("defaut")
            case "multidimensional" :
                if way == "chubeas" :
                    way = way+"/"+file
                    file = ch
                n,ksc,ndim,list_objects = load_multi(way,file)
                match al:
                    case "brute_force" :
                        t,obj,value = bruteForce.bruteForceMultiDimensional(ksc,list_objects)
                    case "greedy_value" :
                        t,obj,value = greedyV.greedy_value_multi(list_objects,ksc)
                    case "greedy_weight" :
                        t,obj,value = greedyW.greedy_weight_multi(list_objects,ksc)
                    case "greedy" :
                        t,obj,value = greedy.greedy_multi(list_objects,ksc)
                    case "grasp" :
                        if str(self.nb_iter.get()).isnumeric() :
                            nb = int(self.nb_iter.get())
                        else :
                            nb = 30
                        t,obj,value = grasp.grasp_multi(list_objects, nb, ksc)
                    case "comp" :
                        tmp = self.checklist.getCheckedItems()
                        self.compF.append(file)
                        for a in tmp :
                            match a :
                                case "brute_force" :
                                    t,obj,value = bruteForce.bruteForceMultiDimensional(ksc,list_objects)
                                    self.comp["brute_force"].append(t)
                                case "greedy_value" :
                                    t,obj,value = greedyV.greedy_value_multi(list_objects,ksc)
                                    self.comp["greedy_value"].append(t)
                                case "greedy_weight" :
                                    t,obj,value = greedyW.greedy_weight_multi(list_objects,ksc)
                                    self.comp["greedy_weight"].append(t)
                                case "greedy" :
                                    t,obj,value = greedy.greedy_multi(list_objects,ksc)
                                    self.comp["greedy"].append(t)
                                case "grasp" :
                                    nb = 30
                                    t,obj,value = grasp.grasp_multi(list_objects, nb, ksc)
                                    self.comp["grasp"].append(t)
                    case _ :
                        print("defaut")



        o = ""
        if len(obj)> 100 :
            tmp = obj[-10:]
            obj = obj[:10]
            obj.append("...")
            for i in tmp :
                obj.append(i)

        for i in obj :
            o = o + " " + str(i)

        self.obj.configure(wraplength=1000)

        self.time.configure(text="Time (s) : " + str(t))
        self.time.grid(column=175,row=12)

        self.obj.configure(text="Objects : " + o)
        self.obj.grid(column=175,row=13)

        self.value.configure(text="Value : " + str(value))
        self.value.grid(column=175,row=14)

    def clear(self,*args):
        self.comp = {"ant_colony":[],"branch_and_bound":[],"brute_force":[],"dynamic_programming":[],"greedy_value":[],"greedy_weight":[],"greedy":[],"grasp":[],"polynomial":[],"personal":[]}
        self.compF = []
    
    def show(self,*args):
        if self.compF:
            graph.graph(self.comp, self.compF)

def load(way,file):
    path = "test_files/" + way + "/"+ file
    with open(path, "r") as f:
        data = f.read()
        line = data.split("\n")
    # We will collect the data
    # First with the number of object and the capacity of the knapsack
    nbo, ksc = line[0].split()
    n = int(nbo)  # number of object
    wmax = int(ksc)  # Maximum weight
    # Proceeding every object and giving the time needed to process the file
    list_objects = []
    for i in range(1, n+1):
        oval, owei = line[i].split()
        list_objects.append((int(oval), int(owei)))
    return n,wmax,list_objects

def load_multi(way,file):
    path = "test_files/All-MKP-Instances/" + way + "/"+ file
    with open(path, "r") as f:
        data = f.read()
        line = data.split("\n")

    # Starting to gather data
    nbo, ndim, opti_sol = line[0].split()

    n = int(nbo)
    ndim = int(ndim)
    ksc = []
    # In order to gather one object at a time
    object = []

    # Receiving container
    list_objects = []

    # Checking all objects
    acc = 0
    i = 0
    for l in line[1:]:
        for w in l.split() :
            # Including all object with their profit
            if len(list_objects) < n:
                object = (int(w), [])
                list_objects.append(object)

            # Imputing all other data
            else:
                if i < n:
                    # Getting every weight for every dimension
                    list_objects[i][1].append(int(w))
                    acc+=1
                    # We got every weight of object i
                    if acc == ndim:
                        acc = 0
                        i+=1
                else :
                    # Getting the knapsack capacity               
                        ksc.append(int(w))

                    
    return n,ksc,ndim,list_objects

root = tk.Tk()
App(root)
root.mainloop()
