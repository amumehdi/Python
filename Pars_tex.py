import matplotlib.pyplot as plt
import numpy as np
import re
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

FileName='sdddd.txt'
Fields=["F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12",]
F1=[]
F2=[]
F3=[]
F4=[]
F5=[]
F6=[]
F7=[]
F8=[]
F9=[]
F10=[]
F11=[]
F12=[]

f=open(FileName,"r")
FirstLine=f.readline()
FieldsNum=len(FirstLine.split(" "))
DataLines=f.readlines()
DataAll=[0]*len(DataLines)
line_counter=0
VarOut=[0]*FieldsNum
for i_list in DataLines:
    i_list=i_list.strip('\nn')               # but it is useless ! it doens't strip
    line_in_string=i_list.split(" ")
    line_in_float=[0]*FieldsNum
    float_counter=0
    for number_string in line_in_string:
        line_in_float[float_counter]=float(number_string)
        str2eval=Fields[float_counter]+'.append(float(number_string))'
        eval(str2eval) 
        float_counter=float_counter+1
    DataAll[line_counter]=line_in_float
    line_counter=line_counter +1



print(DataAll[2][4])
print(DataAll[1][9])
X=np.arange(0,len(F1),1)

fig, ax = plt.subplots()  # Create a figure and an axes.
plt.plot(np.arange(0,len(F1),1),F1)
plt.show()
eval('print(DataAll[1][9])')