print("1. Take 5 numbers as input and store in a list")
num = int(input("Enter the number of elements in the list :"))
a=[]
for i in range(num):
    val=input("enter the elements :")
    a.append(val)
print("list",a)


print("2. Find the max and min in the list")
num = int(input("Enter the number of elements in list :"))
a=[]
for i in range(num):
    val=input("enter the elements :")
    a.append(val)
a.sort()
print("The min value in list :",a[0])
print("The max value in list :",a[-1])


print("3. Remove duplicates from a list")
num = int(input("Enter the number of elements in list :"))
a=[]
for i in range(num):
    val=input("enter the elements :")
    a.append(val)
b=list(set(a))
print("The unique list: ",b)


print("4. Reverse a list without using reverse()")
num= int(input("Enter the number of input :"))
a=[]
for i in range(num):
    val=input("Enter the input:")
    a.append(val)
b=a[::-1]
print("The reversed list :",b)