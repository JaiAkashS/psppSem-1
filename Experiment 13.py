n=int(input("Enter the size:"))
a=[]
for i in range(0,n):
      b=input("Enter Element:")
      a.append(b)
def maximum(l):
      max=l[0]
      for i in range(0,len(l)):
                  if(max<a[i]):
                         max=l[i]
      return max
print(a)
print(maximum(a))
