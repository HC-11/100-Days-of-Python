#average life span = 90 years
# 1 Year = 365 days, 52 weeks, 12 months

# 🚨 Don't change the code below 👇
from email import message


age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_as_int = int(age)
years_remaining = 90 - age_as_int
months_reamining = years_remaining * 12
weeks_reamining = years_remaining * 52
days_remaining = years_remaining * 365
message = f"You have {days_remaining} days, {weeks_reamining} weeks, and {months_reamining} months left."
print(message)