import matplotlib.pyplot as plt
import numpy as np

ENC_MAX=26240

Enc=range(1,ENC_MAX)
down_coef=[ 2.74668e-17, -4.71125e-11, 0.00593861, 68.3226]
up_coef=[3.81871e-17, -5.75944e-11, 0.00594275, 68.1941]

DownPoly=[]
UpPoly=[]
errorPoly=[]
downval=0
upval=0
error=0
for i in Enc:
    downval= i*i*i*down_coef[0]+i*i*down_coef[1]+i*down_coef[2]+down_coef[3]
    #downval=np.polyval(down_coef,i)
    DownPoly.append(downval)
    upval=i*i*i*up_coef[0]+i*i*up_coef[1]+i*up_coef[2]+up_coef[3]
    UpPoly.append(upval)
    error=upval-downval
    errorPoly.append(error)
# %%
error_coef=np.polyfit(Enc[:],errorPoly,1)
errorpoly1d=np.poly1d(error_coef)
errorp=np.linspace(1,ENC_MAX,ENC_MAX)

fig=plt.figure(1)
plt.plot(Enc[:],UpPoly,label="IncPoly")
plt.plot(Enc[:],DownPoly,label="DecPoly")
plt.plot(Enc[:],errorPoly,label="error")
plt.plot(errorp,errorpoly1d(errorp),label="errorpoly")
plt.legend()
plt.grid()
plt.ylabel('mm') 
plt.xlabel('encoder tick')

plt.show()
plt.close()
