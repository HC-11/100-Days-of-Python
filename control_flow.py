print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age <= 18:
      print("Your ticket will cost $7")
  else:
      print("Your ticket will cost $12")
else:
  print("You can't ride the rollercoaster")
print(" --------------------------------- ")

print(" --------------------------------- ")

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number%2 == 0:
  print("Your number is even")
else:
  print("Your number is odd")
