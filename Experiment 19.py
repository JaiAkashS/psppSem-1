with open("File1.txt",'r') as f1:
       with open("File2.txt",'w') as f2:
              data=f1.readlines()
              f2.writelines(data)
f2=open('File2.txt','r')
data=f2.readlines()
print(data)




