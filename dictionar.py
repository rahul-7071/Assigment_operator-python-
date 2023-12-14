# Q1:- Write a Python script to add a key to a dictionary.
# solution Below------------------------------------>



# 2. Write a Python program to concatenate following dictionaries  to create a new one.
'''
d1={1:100, 2:200}
d2={3:300, 4:400}
d3={5:500, 6:600}
d4={}
d4.update(d1)
d4.update(d2)
d4.update(d3)
print(d4)
'''

# 3. Write a Python program to check if a given key already exists 
#    in a dictionary.
'''
dic={1:"rahul",2:"singh",3:"hello"}
key=int(input("Enter your key:"))
for i in dic:
    if key==i:
        print("Yessss")
        break
'''




# Q4:-Write a Python script to print a dictionary where the keys are 
#    numbers between 1 and 15 (both included) and the values are square of keys.
'''
st={}
for i in range(1,15):
    st[i]=i**2
print(st)
'''


# Q5:-Write a Python program to sum all the items in a dictionary
'''
dic={1:7,2:6,4:5}
sum=0;
for i in dic:
    sum=sum+dic[i]
print(sum)
'''

# Q6:- Write a Python program to remove a key from a dictionary.
'''
remove_key= {'a':1,'b':2,'c':3,'d':4}
remove_key.pop('b')
print(remove_key)
'''

# Write a Python program to sort a dictionary by key.
'''
dic={2:4,1:5}
lis=list(dic.keys())
lis.sort()
for i in lis:
    print(i,":",dic[i])
'''

# Q:-8. Write a Python program to remove duplicate values from  Dictionary.
'''
dic={1:2,8:3,3:6,4:3}
lis=list(dic.values())
for i in range(0,3):
    for j in range(i+1,3):
        if lis[i]==lis[j]:
            lis.pop(i)

print(lis)
'''


# Q:-9 Write a program to determine frequency of number in a list of numbers.
# solution Below-------------------------------->
# lis=[2,3,4,65,76,8,5,5,34,2,334,35,]
# print(lis.count(5))