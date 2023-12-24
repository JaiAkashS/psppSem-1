f1=open('File1.txt','r')
data=f1.read()
word=data.split()
f1.close()
print(word)
print('Length',len(word))


