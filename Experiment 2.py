unit=int(input("Enter The Amout Of Unit Used: "))
if(unit<=100):
      rate=(unit*0.75)+20
elif(unit>100&unit<=500):
      rate=(100*0.75)+((unit-100)*1.25)+20
else:
      rate=(100*0.75)+(400*1.25)+((unit-500)*3.25)+20
print("EB Bill =",rate,"for ",unit,"units")
      
      










 







