#Data Types

#String
print("Hello"[0])
#Integer
print(12345 + 54321)
#Float
avogrado = 6_022_140.76
print(avogrado)
#Boolean
False
True
"""
This is a multiline comment in Python
This type of comment is sometimes called a docstring.
A docstring starts with three double-quotation marks, and also ends with three
double quotation marks
 
"""
#-----------------------------------------
#Concatenating different variables
# num_char = len(input("What is your name?"))
#Function that converts integer into string
# new_num_char = str(num_char)
# print("Your name is "+new_num_char+" characters long")
#-----------------------------------------

#Converting a variable into another
a = str(123) #print(type(a)) -> class int
print(type(a)) # -> class str
b = float(616)
print(type(b)) # -> class float
print(70 + float("100.5"))
print(str(70)+str(100))

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
num_a = two_digit_number[0]
num_b = two_digit_number[1]
print(int(num_a)+int(num_b))
