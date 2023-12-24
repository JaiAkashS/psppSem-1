num=int(input("Enter a num:"))
def fact(n):
      factorial=1
      if n==0:
            return 1
      else:
            factorial=n*fact(n-1)
            return factorial

     
print("The Factorial of the Number is :",fact(num))
      
