print("1. Create a dictionary of student names and marks")
dic={}
num = int(input("Enter the number of students :"))
for i in range(num):
    name=input("Enter student name :")
    marks=float(input("Enter marks :"))
    dic[name]=marks
print(dic)


print("2. Print only students who scored above 80")
dic={}
num=int(input("enter the number of students :"))
for i in range(num):
    name=input("Enter the students name :")
    marks=float(input("enter the marks :"))
    dic[name]=marks
student=[]
for name,marks in dic.items():
    if marks>=80:
        student.append(name)
print("The students who scored above 80 marks :",student)


print("3. Add a new student to the dictionary")
dic={}
num=int(input("Enter the number of inputs :"))
for i in range(num):
    name=input("Enter the students name :")
    marks=float(input("Enter the marks :"))
    dic[name]=marks
num=int(input("Enter the number of inputs to be updated :"))
for i in range(num):
    name1=input("Enter the students name to be added:")
    marks1=float(input("Enter the marks to be added :"))
    dic[name1]=marks1
    print("The updated dictionary :",dic)
