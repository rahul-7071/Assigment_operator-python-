#Q1: write a python program that read a string from a user and print the string in double quotation marsk
# solution of Q1--------->
'''
str=input("Enter your String: ")
   print('"',str,'"')
print(f'"{str}"')
'''



# Q2: Write a Python program which accepts the radius of a circle from the user and compute the area.
# solution of Q2--------->
'''
radius=eval(input("Enter the radius:"))
print(f"Area of the Cirle with Radius {radius} is",3.14159*radius*radius)
'''

# Q3: Write a Python program that will accept the base and height of a triangle and compute the area.
# solution of Q3--------->
'''
base=eval(input("Enter the Base of the Triangle:"))
height=eval(input("Enter the Base of the Height:"))
print(f"Area of the Triangle with height {height} and Base {base} is :",(base*height)/2)
'''



# Q4: Write a Python program to perform swapping of two numbers with or without third variable.
# solution of Q4--------->
'''
num1=eval(input("Enter your first Number: "))
num2=eval(input("Enter your second Number: "))
# temp=num1
# num1=num2
# num2=temp
num1,num2=num2,num1 #without third variable
print(f"After swappint First Number is {num1} and Second Number is {num2}")
''''


# Q5: Write a Python program that read a 3 digit number from user and perform the addition of their digits.
# solution of Q5--------->
'''
num=input("Enter three digit Number:")
sum=0;
if(len(num)<4 and len(num)>0):
    for i in num:
     sum+=int(i)
    print(f"Sum of {num} Is ",sum)
else:{
   print("Kindly Enter three Digit Number")
}
'''

# Q6: Write a python program to find the greatest number among three.
# solution of Q6--------->
'''
num1=eval(input("Enter first Number:"))
num2=eval(input("Enter second Number:"))
num3=eval(input("Enter third Number:"))
if num1>num2 and num1>num3:
    print(f"{num1} is Gretest")
elif num2>num1 and num2>num3:
    print(f"{num2} is Greatest")
else:{
    print(f"{num3} is Greatest")
}
'''

# Q7:Write a python program to display a greet message according to the marks obtained by the student.
# solution of Q7--------->
'''
marks=int(input("Enter Your Marks :"))
if marks<=100 and marks>=90:
    print(f"Congratulation for {marks} marks")
elif marks<90 and marks >=60:
    print("First Division")
elif marks<60 and marks>=40:
    print("Pass")
elif marks<40 and marks>=30:
    print("Second")
else:{
    print("fail")
}
'''

# Q8:-Enter basic salary from the user. Write a program to calculate DA and HRA on the following conditions:
# <=2000
# 10%
# 20%

# >2000 && <=5000
# 20%
# 30%

# >5000 && <=10000
# 30%
# 40%
# >10000
# 50%
# 50%

# solution of Q8--------->
'''
user_salary=int(input("Enter Your salary:"))
DA=0
HRA=0
if(user_salary<=2000 and user_salary>0):
    DA=(user_salary*10)/100
    HRA=(user_salary*20)/100

elif(user_salary>=2000 and user_salary<=5000 and user_salary>0):
    DA=(user_salary*20)/100
    HRA=(user_salary*30)/100
elif(user_salary>5000 and user_salary<=10000 and user_salary>0):
    DA=(user_salary*30)/100
    HRA=(user_salary*40)/100
else:
    DA=(user_salary*50)/100
    HRA=(user_salary*50)/100
print(f"Your salary is {user_salary}\nDA={DA} and HRA={HRA}")
'''
