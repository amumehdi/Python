# %%
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
    i_list=i_list.strip('\n')               # but it is useless ! it doens't strip
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

# %%

def add_int_decimal(x_f,x_decimal):
    return float(int(x_f)+x_decimal/10000)

x_precise= list(map(add_int_decimal, F1, F11 ))
y_precise= list(map(add_int_decimal, F2, F12 ))

error_x_map= map(lambda xg, xr: xg-xr, x_precise, F5)
error_y_map= map(lambda yg, yr: yg-yr, y_precise, F6)
error_x=list(error_x_map)
error_y=list(error_y_map)


# %%
####### these should always remain the same
fig1=plt.figure(1) # Create a figure and an axes.
#plt.plot(np.arange(0,len(F1),1),F1,label="tcp Position x")
#plt.plot(np.arange(0,len(F2),1),F2,label="tcp Position y")
plt.plot(np.arange(0,len(x_precise),1),x_precise,label="tcp x precise")
plt.plot(np.arange(0,len(y_precise),1),y_precise,label="tcp y precise")

#plt.plot(np.arange(0,len(F3),1),F3,label="tcp Position z")
#plt.plot(np.arange(0,len(F4),1),F4,label="tcp Position Theta")
plt.plot(np.arange(0,len(F5),1),F5,label="Ref Position x")
plt.plot(np.arange(0,len(F6),1),F6,label="Ref Position y")
#plt.plot(np.arange(0,len(F7),1),F7,label="Ref Position z")
#plt.plot(np.arange(0,len(F8),1),F8,label="Ref Position theta")
plt.legend()
plt.grid()
#plt.ioff()
plt.ylabel('Values') 
plt.xlabel('Samlpes')

# %%
fig2=plt.figure(2)
plt.plot(x_precise,y_precise,label="Goliath Trajectory")
plt.plot(F5,F6,label="Generated Refrence")
plt.legend()
plt.grid()
plt.ylabel('Y') 
plt.xlabel('X')
# %%
fig3=plt.figure(3)
plt.plot(np.arange(0,len(error_x)), error_x, label="error x ")
plt.plot(np.arange(0,len(error_y)), error_y, label="error y ")
plt.legend()
plt.grid()
plt.ylabel('Y') 
plt.xlabel('X')
# %%
#######

#plt.plot(np.arange(0,len(F9),1),F9,label="goliathPos.theta")
#plt.plot(np.arange(0,len(F10),1),F10,label="theta_odo_accu_filt")
#plt.plot(np.arange(0,len(F11),1),F11,label="x decimal ")
#plt.plot(np.arange(0,len(F12),1),F12,label="y decimal")
plt.show()
plt.close()


