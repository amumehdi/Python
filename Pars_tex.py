import matplotlib.pyplot as plt
import numpy as np
import re
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
Filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(Filename)
f=open(Filename)
FirstLine=f.readline()
FieldsNum=len(FirstLine.split(" "))
DataLines=f.readlines()
f.close()
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
plt.plot(np.arange(0,len(F1),1),F1,label="Goliath Position x")
plt.plot(np.arange(0,len(F2),1),F2,label="Goliath Position y")
#plt.plot(np.arange(0,len(F3),1),F3,label="Goliath Position z")
#plt.plot(np.arange(0,len(F4),1),F4,label="Goliath Position Theta")
#plt.plot(np.arange(0,len(F5),1),F5,label="Ref Position x")
#plt.plot(np.arange(0,len(F6),1),F6,label="Ref Position y")
#plt.plot(np.arange(0,len(F7),1),F7,label="Ref Position z")
#plt.plot(np.arange(0,len(F8),1),F8,label="Ref Position Theta")
plt.plot(np.arange(0,len(F9),1),F9,label="Odo Filt X")
plt.plot(np.arange(0,len(F10),1),F10,label="Odo Filt Y")
plt.plot(np.arange(0,len(F11),1),F11,label="Sensor Filt X")
plt.plot(np.arange(0,len(F12),1),F12,label="Sensor Filt y")
plt.legend()
plt.ylabel('Values') 
plt.xlabel('Samlpes')
plt.show()
eval('print(DataAll[1][9])')
