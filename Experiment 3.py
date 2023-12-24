import math
x=int(input("Enter The Value of x:"))
n=int(input("Enter The No. of n:"))
x=(3.14*x)/180
s=0
sign=1
for i in range(1,n*2,2):
    s=s+((x**i)/math.factorial(i))*sign
    sign=sign*-1
print(s)