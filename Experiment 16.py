import pandas as pd
a=[1,2,3]
m1=pd.Series(a)
m2=pd.Series(a,index=['a','b','c'])
print("Series\n",m1)
print("Custom Index\n",m2)
dict1={"Calorie":[100,200,300],"Time":[10,15,25]}
m4=pd.DataFrame(dict1)
print("DataFrame\n",m4)
print("Loc[0]\n",m4.loc[0])
m4.info()
print("Shape\n",m4.shape)
