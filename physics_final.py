import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import os
os.system('cls')


print("\t\t\t\t --------------------------------- \t\t\t\t")
print("\t\t\t\t Experiment on Dielectric Constant \t\t\t\t")
print("\t\t\t\t --------------------------------- \t\t\t\t")
print(" ")
print("Objective      : To study the variation of dielectric constant with temperature and to find the Curie's temperature of given sample.")
print(" ")
print("Apparatus Used : Sample of Barium Titanate(BaTiO3), probe arrangement, oven, oven controller, digital capacitance meter.")
print(" ")
print("Formula Used   : Er = C/Co")

A = 48*pow(10, -3)
T = 1.42*pow(10, -3)
Eo = 8.85*pow(10, -3)

# Calculating the value of Co :
Co = (Eo*A)/T
print(" ")
print("Value of Co is :", '%.3f' % Co, "pF")
print(" ")

choice = 0
print("How do you want to provide data : ")
print("1. Input Manually.")
print("2. Import from pre-existing data set.")
print(" ")
choice = int(input("Enter your choice : "))
print(" ")


lst = []
path = "data-main.xlsx"

if (choice == 1):
    r = int(input("Number of readings : "))
    print(" ")
    print("Enter Temperature(T) in °C and Capacitance(C) in pF.")
    print(" ")
    for i in range(r):
        row = []
        for j in range(2):
            if (j == 0):
                elem = int(input("Temperature "+str(i+1)+" : "))
                row.append(elem)
            else:
                elem = int(input("Capacitance "+str(i+1)+" : "))
                row.append(elem)
        lst.append(row)
        print(" ")
else:
    xl = pd.read_csv("datacsv.csv")
    lst = xl.values.tolist()

print("Processing the dielectric constant for each reading....... ")
time.sleep(1.3)
print("Generating table......")
time.sleep(1.3)
print(" ")


# for printing Observation Table
lst2 = []
for i in range(len(lst)):
    dielectric = float(lst[i][1]/0.299)
    lst2.append(dielectric)

print("\t\t\t|  ", "S.No", "|", "    Temperature °C", "\t|",
      "   Capacitance (pF)", "\t|", "Dielectric Constant (E)|")
for i in range(len(lst)):
    if (i < 9):
        print("\t\t\t|   ", (i+1), "  |\t  ", lst[i][0],
              "\t\t|\t ", lst[i][1], "\t\t|\t", '%.2f' % lst2[i], "  \t |")
    else:
        print("\t\t\t|  ", (i+1), "  |\t  ", lst[i][0],
              "\t\t|\t ", lst[i][1], "\t\t|\t", '%.2f' % lst2[i], "  \t |")
print(" ")

# Curie's Temperature
max_dc = max(lst2)
index = lst2.index(max_dc)
curie = lst[index][0]

# for plotting graph
temp = []  # x
dc = []  # y

for i in range(len(lst)):
    temp.append(lst[i][0])
    dc.append(lst2[i])

print("Plotting Graph......")
time.sleep(1.3)
print("Graph Plotted Successfully......")
print(" ")
time.sleep(1.3)

plt.plot(temp, dc)
plt.xlabel("Temperature °C")
plt.ylabel("Dielectric Constant (E)")
plt.title("Dielectric Constant v/s Temperature")

print("Analyzing Graph......")
print(" ")
time.sleep(1.3)

print("Curie's Temperature of given material(BaTiO3) : ", curie, " (approx)")
print(" ")
print("END Of EXPERIMENT")
print(" ")
print(" ")

plt.show()
