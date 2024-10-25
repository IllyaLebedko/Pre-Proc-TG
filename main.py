import tkinter as tk
from tkinter import filedialog
import csv

def squareTriangle(a, b):
    firstBraсket = a[0]*b[1]+a[1]*b[2]+a[2]*b[0]
    secondBraсket = b[0]*a[1]+b[1]*a[2]+b[2]*a[0]
    return (firstBraсket-secondBraсket)/2

file_path = filedialog.askopenfilename()

time = []
value = []
with open(file_path, newline='') as file:
    reader = csv.reader(file,delimiter=';')
    for row in reader:
        time.append(float(row[0]))
        value.append(float(row[1]))

allS = []
eps = (max(value)-min(value))/100
newTime = [time[0], time[1]]
for i in range (0,len(time)-2):
    for j in range(i+1,len(time)-2):
        time3 = (time[i],time[j],time[j+1])
        value3 = (value[i],value[j],value[j+1])
        if abs(squareTriangle(time3, value3)) > eps:
            newTime.append(time[j])
            #i = j
        break

newTime.append(time[len(time)-1])
    
print(newTime)