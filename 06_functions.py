print("2. Write a function to calculate factorial")
def factorial(num):
    fact=1
    if num<0 :
        print("Factorial doesn't exist!")
    elif num==0:
        print("the factorial is :1")
    else:
        for i in range(1,num+1):
            fact=fact*i
        return fact
number=int(input("Enter a number:"))
print("the factorial of entered number : ",factorial(number))


print("3. Write a function to find the sum of a list")
def sum(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum
num=int(input("Enter the number of elements in the array:"))
a=[]
for i in range(num):
    val=int(input("enter the elements:"))
    a.append(val)
print("the sum of all elements :",sum(a))


print("4. Recursive function for factorial (optional)")
def factorial(num):
    if num < 0:
        print("The factorial doesn't exist.")
        return None  # explicitly return something
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
number = int(input("Enter the number: "))
result = factorial(number)
if result is not None:
    print("The factorial of the required number:", result)


print("1. Write a function to check if number is prime")
import math
def prime(num):
    f=0
    if num<=1:
        f=1
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num % i==0:
                f=1
                break
        if f==0 :
            return "the number is prime"
        else:
            return "the number is not prime"
number = int(input("enter the number :"))
result=prime(number)
print(result)



    

