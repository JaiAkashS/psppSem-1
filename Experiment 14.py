s=input("Enter a string:")
new_string=''
for i in s:
    new_string=i+new_string
print(new_string)
if(new_string==s):
      print("The given string is a Palindrome")
else:
      print("The given string is not a Palindrome")
