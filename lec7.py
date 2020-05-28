"""
Lecture 7 while loops
"""

i = 5 

while i >= 0:
    
    try:
        print(1/(i-3))
    
    except:
        pass
    i = i -1
'''    
    i = i-1
    
    if i == 3:
        pass
    print(i)
'''
'''
for word in "hello world".split():
    print(word)
    
    for str_item in word:
        
        if str_item == 'l':
            break
        print(str_item)
'''
        
'''
try:
    print(1/0)
except ZeroDivisionError:
    print('division by error')
'''
