print("1. Handle divide by zero using try-except")
print("2. Ask the user to enter an integer — handle wrong input")
print("3. Use `finally` to always print “Thanks for using this program”")
try:
    num=int(input("Enter the numerator :"))
    din = int(input("Enter the dinominator :"))
    div=num/din
except ValueError :
    print("Invalid Input.")
except ZeroDivisionError as err:
    print(err)
else:
    print("The answer is :",div)
finally:
    print("Thanks for using this program")




