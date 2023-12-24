tempList=[]
n=int(input("Enter Size of Set:"))
for i in range(n):
    tempList.append(input("Enter Elements:"))
set1=set(tempList)
print(set1)
print("1.Insert\n2.Update\n3.Check\n4.Delete\n5.Union",
        "\n6.Difference\n7.Intersection\n8.Delete a Set",
          "\n9.Frozen Set\n10.Exit")
while(exit):
    choice=int(input("Enter Choice:"))
    if(choice==1):#Insert
        temp=input("Enter Element:")
        set1.add(temp)
        print(set1)
    elif(choice==2):#Update
        n=int(input("Enter Size of Set:"))
        for i in range(n):
            tempList.append(input("Enter Elements:"))
        set2=set(tempList)
        set1.update(set2)
        print(set1)
    elif(choice==3):#Check
        temp=input("Enter Element:")
        if(temp in set1):
            print("Element is Present")
        else:
            print("Element not Present")
    elif(choice==4):#Delete
        temp=input("Enter Element:")
        set1.remove(temp)
        print(set1)
    elif(choice==5):#union
        n=int(input("Enter Size of Set:"))
        tempList=[]
        for i in range(n):
            tempList.append(input("Enter Elements:"))
        set3=set(tempList)
        print('Union',set1.union(set3))
    elif(choice==6):#Difference
        n=int(input("Enter Size of Set:"))
        tempList=[]
        for i in range(n):
            tempList.append(input("Enter Elements:"))
        set3=set(tempList)
        print('Difference',set1.difference(set3))
    elif(choice==7):#Intersection
        n=int(input("Enter Size of Set:"))
        tempList=[]
        for i in range(n):
            tempList.append(input("Enter Elements:"))
        set3=set(tempList)
        print('Intersection',set1.intersection(set3))
    elif(choice==8):#Delete a Set
        set1.clear()
        print(set1)
    elif(choice==9):#FrozenSet
        n=int(input("Enter Size of Set:"))
        tempList=[]
        for i in range(n):
            tempList.append(input("Enter Elements:"))
        set3=frozenset(tempList)
        print('FrozenSet',set3)
    elif(choice==10):#Exit
        exit=False 
    else:
        print("Enter Proper Choice!")

