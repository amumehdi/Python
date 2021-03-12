import matplotlib.pyplot as plt
f=open('..\sdddd.txt',"r")
VarNames=["a","b","c","d","e","f","g"]

Data=f.readlines()
counter=0
for i_list in Data:
    counter=counter +1
    V=(i_list.split(" ")).strip(" \n")
