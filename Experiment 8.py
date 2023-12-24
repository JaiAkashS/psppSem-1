books=[]
books2=[]
n=int(input("Enter Size of Library:"))
for i in range(n):
    books.append(input("Enter Books:"))
print(books)
print("1.Inserting a Book\n2.Deleting\n3.Maximum\n4.Minimum\n5.Sorting\n6.Concatenating\n7.Exit")
exit=True
while(exit):
    choice=int(input("Enter Choice:"))
    if(choice==1):
        temp=str(input("Enter Book To Insert:"))
        tempIndex=int(input("Enter Index:"))
        books.insert(tempIndex,temp)
        print(books)
    elif(choice==2):
        temp=str(input("Enter Book To Delete:"))
        books.remove(temp)
        print(books)
    elif(choice==3):
        print("Maximum:",max(books))
    elif(choice==4):
        print("Minimum:",min(books))
    elif(choice==5):
        books.sort()
        print("Sorted Books:",books)
    elif(choice==6):
        n=int(input("Enter Size of second Library:"))
        for i in range(n):
            books2.append(input("Enter Books:"))
        books=books+books2
        print(books)
    elif(choice==7):
        exit=False
    else:
        print("Enter Proper Choice!")
