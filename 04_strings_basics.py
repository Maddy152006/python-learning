print("1. Reverse a string")
string1 = input("Enter a string :")
rev =''
i=0
for i in string1:
    rev = i + rev
print(rev)


print("2. Count number of vowels in a string")
string1= input("Enter any string :")
count=0
i=0
for i in string1:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" :
        count+=1
print("Number of vovels in string :",count)


print("3. Replace all spaces with dashes")
string1=input("Enter a string :")
string2=string1.replace(" ","_")
print(string2)


print("4. Check if a string is a palindrome")
string1 = input("Enter a string: ")
length = len(string1)
flag = True 
for i in range(length // 2):
    if string1[i] != string1[length - 1 - i]:
        flag = False
        break 
if flag:
    print("The word is a palindrome")
else:
    print("The string is not a palindrome")
