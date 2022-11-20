import tkinter as tk
import os
import greedy.greedy_value as greedyV
import greedy.greedy_weight as greedyW
import greedy.greedy as greedy
import ant_colony.ant_colony as ant
import brute_force.brute_force as bruteForce


class App() :
    def __init__(self,parent) :
        self.parent = parent
        self.entry = tk.Entry(self.parent)

        self.parent.title("knapsack")
        self.parent.geometry("1000x500")

        self.knapsnack_problem = ["0/1","multidimensional"]
        self.type_file = ["low-dimensional","large_scale"]
        self.files = [f for f in os.listdir("test_files/low-dimensional")]
        self.algos = ["ant_colony","branch_and_bound","brute_force","dynamic_programming","greedy_value","greedy_weight","greedy"]

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
    
        self.label_files = tk.Label(self.parent, text="Which file do you wish to work on ? ")
        self.label_files.grid(column=175,row=4)

        self.all_files = tk.OptionMenu(self.parent,self.list_files, *self.files)
        self.all_files.grid(column=175,row=5)

        self.label_ant = tk.Label(self.parent, text="How many ants ? (default = 30) ")
        self.nb_ant = tk.Entry(self.parent)

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

        # Result
        self.time = tk.Label(self.parent,text="")
        self.obj = tk.Label(self.parent,text="")
        self.value = tk.Label(self.parent,text="")

    def set_problem(self,*args):
        pb = self.list_knapsnack_problem.get()
        for child in self.parent.winfo_children() :
            child.destroy()
        match pb :
            case "0/1" :
                self.type_file.clear()
                self.type_file.append("low-dimensional")
                self.type_file.append("large_scale")
                self.files = [f for f in os.listdir("test_files/low-dimensional")]
            case "multidimensional" :
                self.type_file.clear()
                self.type_file.append("chubeas")
                self.type_file.append("gk")
                self.type_file.append("sac94")
                self.files = [f for f in os.listdir("test_files/All-MKP-Instances/chubeas")]
        
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

        self.label_ant = tk.Label(self.parent, text="How many ants ? (default = 30) ")
        self.nb_ant = tk.Entry(self.parent)

        self.time = tk.Label(self.parent,text="")
        self.obj = tk.Label(self.parent,text="")
        self.value = tk.Label(self.parent,text="")

    def set_files(self,*args):
        ls = self.list_type_file.get()
        for child in self.parent.winfo_children() :
            child.destroy()
        match ls :
            case "low-dimensional":
                self.files = [f for f in os.listdir("test_files/low-dimensional")]
            case "large_scale":
                self.files = [f for f in os.listdir("test_files/large_scale")]
            case "chubeas" :
                self.files = [f for f in os.listdir("test_files/All-MKP-Instances/chubeas")]
            case "gk" :
                self.files = [f for f in os.listdir("test_files/All-MKP-Instances/gk")]
            case "sac94" :
                self.files = ["None"]
            #/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\ To do

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

        self.label_ant = tk.Label(self.parent, text="How many ants ? (default = 30) ")
        self.nb_ant = tk.Entry(self.parent)

        self.time = tk.Label(self.parent,text="")
        self.obj = tk.Label(self.parent,text="")
        self.value = tk.Label(self.parent,text="")

    def set_algo(self,*args):
        al = self.list_algos.get()
        ls = self.list_files.get()
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

        self.label_files = tk.Label(self.parent, text="Which algorithm do you wish to launch ? ")
        self.label_files.grid(column=175,row=6)

        self.all_algos = tk.OptionMenu(self.parent,self.list_algos, *self.algos)
        self.all_algos.grid(column=175,row=7)

        self.button = tk.Button(self.parent, text="Launch", command=self.launch)
        self.button.grid(column=175,row=10)

        self.label_ant = tk.Label(self.parent, text="How many ants ? (default = 30) ")
        self.nb_ant = tk.Entry(self.parent)

        self.time = tk.Label(self.parent,text="")
        self.obj = tk.Label(self.parent,text="")
        self.value = tk.Label(self.parent,text="")
        
        if al == "ant_colony" :
            self.label_ant.grid(column=175,row=8)
            self.nb_ant.grid(column=175,row=9)

    def launch(self,*args):

        al = self.list_algos.get()
        way = self.list_type_file.get()
        file = self.list_files.get()
        path = "test_files/" + way + "/"+ file
        n,wmax,list_objects = load(path)
        match al:
            case "ant_colony" :
                if str(self.nb_ant.get()).isnumeric() :
                    nb = int(self.nb_ant.get())
                else :
                    nb = 30
                t,obj,value = ant.ant(list_objects,nb,n,wmax)
            case "branch_and_bound" :
                print("à faire")
            case "brute_force" :
                t,obj,value = bruteForce.bruteForce(wmax,list_objects)
            case "dynamic_programming" :
                print("à faire")
            case "greedy_value" :
                t,obj,value = greedyV.greedy_value(list_objects,wmax)
            case "greedy_weight" :
                t,obj,value = greedyW.greedy_weight(list_objects,wmax)
            case "greedy" :
                t,obj,value = greedy.greedy(list_objects,wmax)
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

def load(path):
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

root = tk.Tk()
App(root)
root.mainloop()
