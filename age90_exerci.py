#average life span = 90 years
# 1 Year = 365 days, 52 weeks, 12 months

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Year = 365 days, 52 weeks, 12 months

age = int(age)
days = (90*365) - (365//31)
weeks = (90*52) - (52//age)
months = (90*12) - (age*12)
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
