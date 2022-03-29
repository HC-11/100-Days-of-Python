# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
text_name = name1+name2
lower_case = text_name.lower()

score_true = lower_case.count("t") + lower_case.count("r") + lower_case.count("u") + lower_case.count("e") 
score_love = lower_case.count("l") + lower_case.count("o") + lower_case.count("v") + lower_case.count("e")

#to Concatenate two integers, first you have to turn them into strings
love_score = int(str(score_true) + str(score_love))

if love_score < 10 or love_score > 90:
   print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score >= 50:
   print(f"Your score is {love_score}, you are alright together.")
else:
   print(f"Your score is {love_score}.")


#For Love Scores less than 10 or greater than 90, the message should be:
#print(f"Your score is {score}, you go together like coke and mentos.")

#For Love Scores between 40 and 50, the message should be:
#print(f"Your score is {score}, you are alright together.")

#Otherwise, the message will just be their score. e.g.:
#print(f"Your score is {score}.")