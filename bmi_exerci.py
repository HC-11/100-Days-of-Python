# 🚨 Don't change the code below 👇

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weight = int(weight)
height = float(height)
bmi = weight/(height**2)
print("Your BMI is: ",int(bmi),"\n") # Use , to concatenate string and a float

# to check a variable's type:  print(type(variable))
#bmi_as_int = int(bmi)
#print(bmi_as_int)

print("Rounding a number. Eg. 8/3 \n")
print("8/3 = 2.66666, now it's: ",(round(8/3,2)))
 #,2 -> two decimal places (.67)
print("\n")
print(8//6) # // = the result of the division will be an integer
print("\n")
score = 3
score += 1 # -=, *=, /= -> these also work
print ("Now the score is: ",score)
print("\n")

# Printing different data types = (f-String) -> print(f"blablabla {variable}, bla bla {another variable}")
score1 = 0
height2 = 1.8
winning = True # Capital 'T' and 'F'
print(f"your current score is {score1}, your height is {height2}, you are winning {winning}")
