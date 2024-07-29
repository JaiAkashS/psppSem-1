s = "   fly me   to   the moon  "
count=0
exit = True
i=-1
while(exit):
    if(count>=1):
        if (s[i]==' '):
            exit = False 
    if(s[i]!=' '):
        print(s[i])
        count+=1
    i-=1
print(count)

