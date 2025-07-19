print(" 1. Print numbers from 1 to 10 using a loop")
num = 0
for num in range(10):
    print(num +1)

print("2. Print multiplication table of any number")
num = int(input("enter any number :"))
i=1
while i<=10:
    val= num *i
    print(str(num) + "*" + str(i) + "=" + str(val))
    i+=1


print(" Sum of digits of a number using while loop")
num = int(input("Enter any number :"))
sum=0
while num>0 :
    remainder = num % 10
    sum += remainder
    num = num//10
print("the sum of digits is :",sum)


print("4. Print all even numbers up to 100")
i=1
for i in range(101):
    if i%2==0:
        print(i)
print("all even numbers upto 100 is printed")

