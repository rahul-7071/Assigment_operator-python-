# Q1:-Write a python program to print all natural numbers from 1 to n. - using while loop
# solution Below------------------------->
'''num=int(input("Enter Your Number:"));
i=1
while(num>0):
    print(i)
    i=i+1
    num=num-1;
'''


# Q2:-Write a python program to print all natural numbers in reverse (from n to 1). - using while loop.
# solution Below-------------------->
'''
num=int(input("Enter Your Number:"))
while(num>0):
    print(num)
    num=num-1;
'''


# Q3:-Write a python program to print all alphabets from a to z. - using while loop
# solution Below------------------------------------->
'''pt=97
while(pt <=122):
    print(chr(pt))#converting 'int' value in 'char' so that we can get the value of ascii value
    pt=pt+1
    '''


# Q4:-Write a python program to print all even numbers between 1 to 100. - using while loop
# solution Below----------------------------------->
'''num=1
while(num<=100):
    if num%2==0:
        print(num)
    num+=1
'''
# -----------------------another method------------------->
'''num=2
while(num<=100):
    print(num)
    num=num+2
'''

# Q5:-Write a python program to print all odd number between 1 to 100.
# solution Below-------------------->
'''
for i in range(1,100):
    if i%2!=0:
        print(i)
'''


# Q6:-Write a python program to find sum of all natural numbers between 1 to n.
# solution Below------------------------------->
'''
num=int(input("Enter your Number:"))
if(num>0):
    print(num*(num+1)/2)
else:
    print("Kindly Enter Natural Number!!")
    '''
