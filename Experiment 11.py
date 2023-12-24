dict1={}
n=int(input("Enter Size of Dict:"))
for i in range(n):
    key=input("Enter key:")
    val=input("Enter val:")
    dict1[key]=val
print(dict1)
print("1.Adding Element\n2.Update Element\n3.Accessing Element",
          "\n4.Copying\n5.Length\n6.Sorting\n7.Deleting a Element",
          "\n8.Deleting Dictionary\n9.Exit")
exit=True
while(exit):
    choice=int(input("Enter Choice:"))
    if(choice==1):#Adding Element
        key=input("Enter the key:")
        value=input("Enter the value")
        dict1[key] = value
        print(dict1)
    elif(choice==2):#Update Element
        dict2={}
        n=int(input("Enter Size of Dict2:"))
        for i in range(n):
            key=input("Enter key:")
            val=input("Enter val:")
            dict2[key]=val
        dict1.update(dict2)
        print(dict1)
    elif(choice==3):#Access Element
        temp=input("Enter a key to access:")
        print(dict1[temp])
    elif(choice==4):#copying
        dict3=dict1.copy()
        print("Copied Dict",dict1)
    elif(choice==5):#length
        print("length:",len(dict1))
    elif(choice==6):#sorting
        print(sorted(dict1))        
    elif(choice==7):#delete element
        temp=input("Enter a Key to remove:")
        dict1.pop(temp)
        print(dict1)
    elif(choice==8):#delete dict
        dict1.clear()
        print(dict1)
    elif(choice==9):#Exit
        exit=False
    else:
        print("Enter Proper Choice!")

