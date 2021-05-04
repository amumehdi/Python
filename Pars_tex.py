# %%
import matplotlib.pyplot as plt
import numpy as np
import re
import myFunctions
import struct

#Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12= myFunctions.pars_Qt()
F1lable="_newTower2"
# %%

def add_int_decimal(x_f,x_decimal):
    return float(int(x_f)+x_decimal/10000)

""" 
def add_int_decimal_refx(xf,z):
    z=int(z)
    z=z&0xFF
    return xf+float(z/256)

def add_int_decimal_refy(yf,z):
    z=int(z)&0xFF00
    z=z/256 # to move 8 bit to the left 
    return yf+float(z/256) 

x_ref_precise = list(map( add_int_decimal_refx, F5, F7))
y_ref_precise = list(map( add_int_decimal_refy, F6, F7))"""

x_precise= list(map(add_int_decimal, F1, F11 ))
y_precise= list(map(add_int_decimal, F2, F12 ))

error_x_map= map(lambda xg, xr: xg-xr, x_precise, F5)
error_y_map= map(lambda yg, yr: yg-yr, y_precise, F6)
error_x=list(error_x_map)
error_y=list(error_y_map)


# %%
####### these should always remain the same
fig1=plt.figure(1) # Create a figure and an axes.
#plt.plot(np.arange(0,len(F1),1),F1,label="tcp Position x"+F1lable)
#plt.plot(np.arange(0,len(F2),1),F2,label="tcp Position y"+F1lable)
plt.plot(np.arange(0,len(x_precise),1),x_precise,label="tcp x precise"+F1lable)
plt.plot(np.arange(0,len(y_precise),1),y_precise,label="tcp y precise"+F1lable)

#plt.plot(np.arange(0,len(F3),1),F3,label="tcp Position z"+F1lable)
plt.plot(np.arange(0,len(F4),1),F4,label="tcp Position Theta"+F1lable)
plt.plot(np.arange(0,len(F5),1),F5,label="Ref Position x"+F1lable)
plt.plot(np.arange(0,len(F6),1),F6,label="Ref Position y"+F1lable)
#plt.plot(np.arange(0,len(F7),1),F7,label="Ref Position z"+F1lable)
plt.plot(np.arange(0,len(F8),1),F8,label="encoder value"+F1lable)
plt.legend()
plt.grid()
#plt.ioff()
plt.ylabel('Values') 
plt.xlabel('Samlpes')

# %%
fig2=plt.figure(2)
plt.plot(x_precise,y_precise,label="Goliath Trajectory"+F1lable)
plt.plot(F5,F6,label="Generated Refrence"+F1lable)
plt.legend()
plt.grid()
plt.ylabel('Y') 
plt.xlabel('X')
# %%
fig3=plt.figure(3)
plt.plot(np.arange(0,len(error_x)), error_x, label="error x "+F1lable)
plt.plot(np.arange(0,len(error_y)), error_y, label="error y "+F1lable)
plt.legend()
plt.grid()
plt.ylabel('mm') 
plt.xlabel('samples')
# %%
#######

fig4=plt.figure(4)
plt.plot(np.arange(0,len(F9),1),F9,'.',label="tower 1"+F1lable)
plt.plot(np.arange(0,len(F10),1),F10,'.',label="tower 2"+F1lable)
#plt.plot(np.arange(0,len(F11),1),F11,label="x decimal"+F1lable)
#plt.plot(np.arange(0,len(F12),1),F12,label="y decimal"+F1lable)
plt.legend()
plt.grid()
plt.ylabel('mm') 
plt.xlabel('samples')

""" 
fig5= plt.figure(5)
plt.plot(np.arange(0,len(x_ref_precise)), x_ref_precise, label="xref precise "+F1lable)
plt.plot(np.arange(0,len(y_ref_precise)), y_ref_precise, label="yref precise "+F1lable)
plt.legend()
plt.grid()
plt.ylabel('mm') 
plt.xlabel('Samples')
 """
plt.show()
plt.close()


