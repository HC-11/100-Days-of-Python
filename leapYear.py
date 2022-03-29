# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check?"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

""" divided by 100 means century year (ending with 00)
 century year divided by 400 is leap year 
 % -> modulus (remainder of a division)"""
 
if (year % 400 == 0) and (year % 100 == 0):
    print(" Leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year 
elif (year % 4 ==0) and (year % 100 != 0):
    print(" Leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year 
else:
    print(" Not leap year".format(year))