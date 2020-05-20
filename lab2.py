"""
Lab 2 Basic Data Types
"""

# Defining string and printing string
my_name = "Tom"
print(my_name.upper())
# Defining int and printing int
my_id = your_id = 123
print(my_id)
print(your_id)
"""
123 = my_id
123 can not be identified as a variable due to the fact that
integers and floats can not be defined as variables
"""
# Defining and printing my_id as a string
my_id_str = "123"
print(my_id_str)

"""
print(my_name + my_id)
You can not perform my_name + my_id due to the fact that
you can not add a string and an integer
"""
# Printing my_name + my_id_str
print(my_name + my_id_str)
print(my_name*3)

#Splitting string
print("hello, world. This is my first python string.".split("."))

#Defining message variable
"""
message = 'Tom's id is 123'
message variable can not be defined by using the single
quotation marks due to the apostorphe in Tom's. Although
the message can be printed using the double quotation marks
(seen below)
"""
message = "Tom's id is 123"
print(message)