# %%
def match_vector(Vref,Vin,index):
   shift=index-Vin.index(Vref[index])
   if shift<=0 :
       shift=abs(shift)
       Vout=Vin[shift:]
       return Vout
   else:
       for x in range(0,shift): Vin.insert(x,0)
       return Vin

def pars_Qt():
    from tkinter.filedialog import askopenfilename
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
    return F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12 

