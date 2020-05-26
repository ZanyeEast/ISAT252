"""
lec 5 python note
"""
"""
y = []
x = None
print(y is None)
print(x is None)
"""
# Boolean data types
# print(True)
#print(False)

# and operator
#print(True and False)

# or operator
#print(True or False)

#not operator
#print(not False)
#print(not True)
#print(not None)
#print(not 0)
#print(() and [])

#Flow Control: if funct, range() funct, for loop, while loop, and continue/ break/ pass
# if statement
'''
if 2>1 :
    print('2>1')
'''
'''
if 2<=1 :
    print('2<=1')
'''
'''
if 2>1 :
    if 1.5>1:
        print('1.5>1')
    print('2>1')
'''
'''
if 2>1 :
    if 1.5<1:
        print('1.5>1')
    print('2>1')
'''

# if-else Statement
'''
if 2<=1:
    print("2<=1")
else:
    print("2>1")
'''
'''
if 2<=2:
    print("2<=2")
else:
    print("2>1")
'''

# if-elif-else Chain
'''
if 2<=1:
    print('2<=1')
elif 2<=2:
    print('2<=2')
else:
    print("2>1")
'''
# The following code prints 3 due to the Fact that None = False, {} is False, and '0' is True
#so 3 is printed first 2 conditions are false so they do not print
'''
if None:
    print(1)
elif {}:
    print(2)
elif '0':
    print(3)
else:
    print(4)
'''