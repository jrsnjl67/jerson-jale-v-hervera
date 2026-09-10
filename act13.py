name = input("Your name:")
age = int(input("Your age:"))

print("You are ")
if age >= 1 and age <=5 :
   print("an Infant")
if age >= 6 and age <= 12:
   print("a Kid")
if age >= 13 and age <= 19:
   print("a Teenager")
if age >= 20 and age <= 29:
   print("in Early adulthood")
if age >= 30 and age <= 48:
   print("an Adult")
if age >= 49 and age <= 59:
   print("an Advance adult")
if age >= 60 and age<= 150:
   print("a Senior")
else:
   print("Invalid")