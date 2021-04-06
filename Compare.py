# %%
import matplotlib.pyplot as plt
import numpy as np
import re
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

#Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
Filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(Filename)
file1=open(Filename)
FirstLine=file1.readline()
FieldsNum=len(FirstLine.split(" "))
DataLines=file1.readlines()
file1.close()
Fields1=["F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12",]
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
        str2eval=Fields1[float_counter]+'.append(float(number_string))'
        eval(str2eval) 
        float_counter=float_counter+1
    DataAll[line_counter]=line_in_float
    line_counter=line_counter +1

# %%
Filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(Filename)
file2=open(Filename)
FirstLine=file2.readline()
FieldsNum=len(FirstLine.split(" "))
DataLines=file2.readlines()
file2.close()
Fields2=["FF1","FF2","FF3","FF4","FF5","FF6","FF7","FF8","FF9","FF10","FF11","FF12",]
FF1=[]
FF2=[]
FF3=[]
FF4=[]
FF5=[]
FF6=[]
FF7=[]
FF8=[]
FF9=[]
FF10=[]
FF11=[]
FF12=[]

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
        str2eval=Fields2[float_counter]+'.append(float(number_string))'
        eval(str2eval) 
        float_counter=float_counter+1
    DataAll[line_counter]=line_in_float
    line_counter=line_counter +1

# %%

def add_int_decimal(x_f,x_decimal):
    return float(int(x_f)+x_decimal/10000)

x1_precise= list(map(add_int_decimal, F1, F11 ))
y1_precise= list(map(add_int_decimal, F2, F12 ))

x2_precise= list(map(add_int_decimal, FF1, FF11 ))
y2_precise= list(map(add_int_decimal, FF2, FF12 ))

error_x1= list(map(lambda xg, xr: xg-xr, x1_precise, F5))
error_y1= list(map(lambda yg, yr: yg-yr, y1_precise, F6))

error_x2= list(map(lambda xg, xr: xg-xr, x2_precise, FF5))
error_y2= list(map(lambda yg, yr: yg-yr, y2_precise, FF6))

# %%
####### these should always remain the same
fig1=plt.figure(1) # Create a figure and an axes.
#plt.plot(np.arange(0,len(F1),1),F1,label="tcp Position x")
#plt.plot(np.arange(0,len(F2),1),F2,label="tcp Position y")
plt.plot(np.arange(0,len(x1_precise),1),x1_precise,label="tcp x50 precise")
plt.plot(np.arange(0,len(y1_precise),1),y1_precise,label="tcp y50 precise")

plt.plot(np.arange(0,len(x2_precise),1),x2_precise,label="tcp x50_wa precise")
plt.plot(np.arange(0,len(y2_precise),1),y2_precise,label="tcp y50_wa precise")

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
plt.plot(x1_precise,y1_precise,label="Goliath Trajectory 50")
plt.plot(x2_precise,y2_precise,label="Goliath Trajectory 50_wa")
plt.plot(F5,F6,label="Generated Refrence")
plt.legend()
plt.grid()
plt.ylabel('Y') 
plt.xlabel('X')
# %%
fig3=plt.figure(3)
plt.plot(np.arange(0,len(error_x1)), error_x1, label="error x50 ")
plt.plot(np.arange(0,len(error_x2)), error_x2, label="error x50_wa ")
plt.plot(np.arange(0,len(error_y1)), error_y1, label="error y50 ")
plt.plot(np.arange(0,len(error_y2)), error_y2, label="error y50_wa ")
plt.plot(np.arange(0,len(F4)), F4, label="theta 50 ")
plt.plot(np.arange(0,len(FF4)), FF4, label="theta 50_wa ")
plt.legend()
plt.grid()
plt.ylabel('error mm') 
plt.xlabel('samples')
# %%
#######
fig3=plt.figure(4)
plt.plot(np.arange(0,len(F9),1),F9,'*',label="Tower1 50")
plt.plot(np.arange(0,len(F10),1),F10,'*',label="Tower2 50")
plt.plot(np.arange(0,len(FF9),1),FF9,'+',label="Tower1 50 wa")
plt.plot(np.arange(0,len(FF10),1),FF10,'+',label="Tower2 50 wa")
#plt.plot(np.arange(0,len(F11),1),F11,label="x decimal ")
#plt.plot(np.arange(0,len(F12),1),F12,label="y decimal")
plt.legend()
plt.grid()
plt.ylabel('mm') 
plt.xlabel('samples')

plt.show()
plt.close()

#def match_vector(Vref,Vin,index):
#    shift=index-Vin.index(Vref[index])
#    if 0<index :
#     return Vin=Vin[shift:]
#    else