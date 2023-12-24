import numpy as np
col=int(input("Enter array col size:"))
row=int(input("Enter array row size:"))
lst=[]
for i in range(row):
    lstItem=[]
    for j in range(col):
        lstItem.append(int(input("Enter Element:")))
    lst.append(lstItem)
arr1=np.array(lst)
print("Array-1:\n",arr1)
print("ndim of Array-1:",arr1.ndim)
col=int(input("Enter array col size:"))
row=int(input("Enter array row size:"))
lst=[]
for i in range(row):
    lstItem=[]
    for j in range(col):
        lstItem.append(int(input("Enter Element:")))
    lst.append(lstItem)
arr2=np.array(lst)
print("Array-2:\n",arr2)
print("Add:\n",arr1+arr2)
print("Multiplication:\n",arr1.dot(arr2))
print("Shape:",arr1.shape)
print("Size:",arr1.size)
print("Max(0)",arr1.max(0))
print("Max(1)",arr1.max(1))
print("Min(0)",arr1.min(0))
print("Min(1)",arr1.min(1))
