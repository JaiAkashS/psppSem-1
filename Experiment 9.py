tempList=[]
n=int(input("Enter Size of Tuple:"))
for i in range(n):
    tempList.append(input("Enter parts:"))
parts=tuple(tempList)
print(parts)
print("1.Changing a Part\n2.Deleting\n3.Concatenating\n4.Maximum\n5.Minimum\n6.Deleting a Tuple\n7.Exit")
exit=True
while(exit):
    choice=int(input("Enter Choice:"))
    if(choice==1):#Changing a Element
        print(parts)
        oldpart=input("Enter part need to be changed:")
        newpart=input("Enter new part:")
        index=parts.index(oldpart)
        tempList[index]=newpart
        parts=tuple(tempList)
        print(parts)
    elif(choice==2):#Deleting
        tempPart=input("Enter part To Delete:")
        tempList.remove(tempPart)
        parts=tuple(tempList)
        print(parts)
    elif(choice==3):#Concatenating
        tempList2=[]
        n=int(input("Enter Size of second Tuple:"))
        for i in range(n):
            tempList2.append(input("Enter parts:"))
        parts2=tuple(tempList2)
        parts=parts+parts2
        print("Parts:",parts)
    elif(choice==4):#Maximum
        print("Maximum:",max(parts))
    elif(choice==5):#Minimum
        print("Minimum:",min(parts))
    elif(choice==6):#Deleting Tuple
        tempList.clear()
        parts=tuple(tempList)
        print("Deleting a Tuple:",parts)
    elif(choice==7):#Exit
        exit=False
    else:
        print("Enter Proper Choice!")
