print("1. Check if a number is even or odd")
num = float(input("Enter a number: "))
if num % 2==0 :
    print("The number is even.")
else:
    print("The number is odd.")


print("2. Grade calculator using marks (90+ = A, etc.)")
marks = float(input("enter ur marks:"))
if marks>90:
    print("Grade A")
elif marks>80 and marks<=90:
    print("Grade B")            
elif marks>70 and marks<=80:
    print("Grade C")
elif marks>60 and marks<=70:
    print("Grade D")
elif marks>50 and marks<=60:
    print("Grade E")
else:
    print("Sorry you failed, better luck next time.")


print("3. Find the largest of three numbers")
num1= float(input("enter the first number :"))
num2= float(input("enter the second number :"))
num3= float(input("enter the third number :"))
if num1>num2 and num1>num3:
    print("The largest number is: " + str(num1))
elif num2>num1 and num2>num3:
    print("The largest number is: " + str(num2))
else:
    print("The largest number is: " + str(num3))


print("4. Check if age is eligible for voting")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
