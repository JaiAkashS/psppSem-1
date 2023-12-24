n=int(input("Enter range :"))
s=0
for i in range(1,n+1):
      s=s+i
      print(i,end='')
      if(i!=n):
            print('+',end='')
print('=',s)


