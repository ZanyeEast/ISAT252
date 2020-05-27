"""
Lab 5
"""
#3.1 assigning alien_color 
alien_color = 'green'
# If statement
if alien_color == 'green':
    print("You've recieved 5 points!")

#3.2 If-else Statement

if alien_color == 'green':
    print("You've recieved 5 points!")
else:
    print("You've recieved 10 points!")

#3.3 list

favorite_fruits = ['mango', 'banana', 'strawberry']

if 'mango' in favorite_fruits:
    print("You really like mangos!")
if 'banana' in favorite_fruits:
    print("You really like bannanas!")
if 'strawberry'in favorite_fruits:
    print("You really like strawberries!")
#False if statements for the five if statements
if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'plum' in favorite_fruits:
    print("You really like plums!")
#3.4 if-elif-else Statement on age and entering my current age (21)
age = 21

if age < 10:
    print("This person is a kid.")
elif age >= 10 > 20:
    print("This person is a teenager.")
else:
    print("This person is an adult.")
    if age >65:
        print("This person is an elder")