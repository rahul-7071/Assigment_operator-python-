# import string
# Q1:-Write a Python program to calculate the length of a string.  
# solution Below---------------------->
'''name="Rahul"
print("Lenght of the given stirng is:",len(name))
'''

# Q2:-Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# solution Below---------------------------->
# name="Beautyful"
# name2=name[0:2]+name[-2:len(name)]
# print(name2)


# Q3:-3 Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# name='abracadabra'
# name2=name.split("a",)
# print(name2)





# 4 Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Ex   Input :    st1=hello  st2=world        
# Expected Output : st3=wollo herld
# str1="hello"
# str2="world"
# ls1,ls2=list(str1),list(str2)
# cut1,cut2=ls1[0:2],ls2[0:2]
# print(cut1)
# stt=str(cut1)
# print(stt)



# Q:-5 Write a Python program to add 'ing' at the end of a given string (length should be at least
# solution Below--------------------------->
'''
ch=input("Enter your string here: ")
print(ch+"ing")

'''


# Q6:- If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
'''
str=input("Enter your Number:")
if len(str)>2:
    if(str.endswith("ing")):
     print(f"{str}ly")
    else:
     print(f"{str}ing")
else:
  print(str)

  '''


# 6 Write a Python program to remove the nth index character from a nonempty string.
# str="rahu kr singh is the most handsome person in this planet"
# str.index(3,9)





#  Write a Python program to remove the characters which have odd index values of a given string.
# str="matihaniya"
# print(str[0:len(str):2])




# 8 Write a Python script that takes input from the user in proper cause and displays that input back in upper and lower cases.
name=input("Enter your string:")
print("Name in Uppercase:-",name.upper())
print("Name in Lowercase:-",name.lower())