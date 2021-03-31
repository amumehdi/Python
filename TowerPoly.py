import matplotlib.pyplot as plt


ENC_MAX=26240

Enc=range(1,ENC_MAX)
down_coef=[ 2.74668e-17, -4.71125e-11, 0.00593861, 68.3226]
up_coef=[3.81871e-17, -5.75944e-11, 0.00594275, 68.1941]

DownPoly=[]
UpPoly=[]
downval=0
upval=0
for i in Enc:
    downval= i*i*i*down_coef[0]+i*i*down_coef[1]+i*down_coef[2]+down_coef[3]
    DownPoly.append(downval)
    upval=i*i*i*up_coef[0]+i*i*up_coef[1]+i*up_coef[2]+up_coef[3]
    UpPoly.append(upval)


fig=plt.figure()
plt.plot(Enc[:],UpPoly,label="IncPoly")
plt.plot(Enc[:],DownPoly,label="DecPoly")
plt.legend()
plt.grid()
plt.ylabel('mm') 
plt.xlabel('encoder tick')

plt.show()
plt.close()
