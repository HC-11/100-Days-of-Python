print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n") 
answer1 = input("Left or right? \n")
if answer1 == "left":
   answer2 = input("swim or wait \n")
   if answer2 == "wait":
      answer3 = input("Which door?\n")
   else: 
      print("Attacked by trout. Game Over.")  
   if answer3 == "yellow":
      print("You Win!\n")
     
   elif answer3 == "blue":
      print("Eaten by beasts. Game Over.")
      
   elif answer3 == "red":
      print("Burned by fire. Game Over.")
   else:
      print("Game Over.")
   
else:
   print("Fall into a hole. Game Over.")
