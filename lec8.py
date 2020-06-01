"""
Lecture 8 Functions
return function should always be the last command in function
"""
'''
#positional argument
def my_function(a, b):
    result = a + b
    print('a is',a)
    print('b is',b)
    return result
print(my_function(2, 1)) 
'''
'''
def my_function(a, b=0):
    result = a + b
    print('a is',a)
    print('b is',b)
    return result
#different way to assign value (key-word argument)
print(my_function(a=2))
'''
'''
def my_function(a, b=0):
    result = a + b
    print('a is',a)
    print('b is',b)
    return a + b
    
print(my_function(a=1)+1)
'''
#Ex1 return absolute value 
'''def calculate_abs(a):
    if type(a) is str:
        return ('wrong data type')
    elif a>0:
        return a
    else:
        return -a
print(calculate_abs(a=0))'''

#ex2 calculate sigma(n,m)
'''def cal_sigma(m,n):
    result = 0 
    for i in range (n,m+1):
        result = result + i
        
    return result

print(cal_sigma(m=5,n=3))'''

'''def cal_pi(n,m):
    result=1
    for i in range(n,m+1):
        result=result*i
    
    return result
print(cal_pi(5,3))'''

#ex3
def cal_f(m):
    if m == 0:
        return 1
    else:
        return m* cal_f(m-1)
#print(cal_f(3))

def cal_p(m,n):
    return cal_f(m)/cal_f(m-n)
print(cal_p(5,3))
    