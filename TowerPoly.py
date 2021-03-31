import matplotlib.pyplot as plt


int(ENC_MAX)=26240

Enc=range(1,ENC_MAX)
down_coef=[ 2.74668e-17, -4.71125e-11, 0.00593861, 68.3226]
up_coef=[3.81871e-17, -5.75944e-11, 0.00594275, 68.1941]

DownPoly=[0]
UpPoly=[0]
downval=0
upval=0
for i in Enc:
    downval= i*i*i*down_coef[1]+i*i*down_coef[2]+i*down_coef[3]+down_coef[4]
    DownPoly.append(downval)
    upval=i*i*i*up_coef[1]+i*i*up_coef[2]+i*up_coef[3]+up_coef[4]
    UpPoly.appen(upval)


fig=plt.figure()
plt.plot(ENC,UpPoly,label="IncPoly")
plt.plot(ENC,DownPoly,label="DecPoly")
plt.legend()
plt.grid()
plt.ion()
plt.ylabel('mm') 
plt.xlabel('encoder tick')

plt.show()
plt.close()
