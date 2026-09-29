import numpy as np # Personalized code for importing \\library 
import matplotlib.pyplot as plt # Python plotting
import math
import numpy as np # importing python's numerical processing package numpy and giving it a short name "np"
import scipy as sp #importing scientific data processing package scipy
#from scipy.optimize import curve_fit #importing curve fitting package
import pandas as pd  # data importation package
from matplotlib import pyplot as plt  # importing plotting environment
import csv
import random
import os

n = 40
eq = 40 # 200 in total
rows = 200

LHS = np.zeros((eq, n))
RHS = np.zeros((eq, 1))
sol = np.zeros((eq, 1))

#print (os.getcwd())

data = pd.read_csv("./HW1Q4/26H01.dat", header=0)

file = open("./HW1Q4/26H01.dat")

content = file.readlines()

#print(data)
#print(content[2])
#exit()

solutionSets = 3000
solArray = np.zeros((solutionSets, eq))

solutionRows = np.zeros((solutionSets, eq))

for i in range(solutionSets):
    solutionRows[i] = random.sample(range(0, 199), eq)

#print(solutionRows)

for i in range(solutionSets):
    if (solutionRows[i].size != eq):
        print("Invalid solution row at ", i)
        exit()


for k in range(solutionSets):
    #exit()
    for i in range(eq):
        #print(i)
       
        eqAdd = int(solutionRows[k][i])
        RHS[i] = int(content[eqAdd + 1][41]) # Slot 41 is just after the | and holds the RHS
        
        for j in range(n):
            LHS[i][j] = int(content[eqAdd + 1][j])

    sol = np.linalg.solve(LHS, RHS)
    for i in range(eq):
        if sol[i] < 0:
            sol[i] = 1
        elif sol[i] > 0:
            sol[i] = 0
        else:
            print("Error.")

    solArray[k] = np.transpose(sol)


#print(solArray)

for i in range(solutionSets):
    for j in range(i+1, solutionSets):
        if (i != j):
            solDiff = solArray[j] - solArray[i]
            if(1 in solDiff or -1 in solDiff):
                #print(i, " : ", j, " : Nope" )
                next
            else:
                print(i, " : ", j, " : Yay" )
