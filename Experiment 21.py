try:
    a = int(input("Enter A:"))
    b = int(input("Enter B:"))
    print("a/b",a/b)
except:
    print("Expection Arised")
else:
    print("No Exceptions")
finally:
    print("Code Executed")
